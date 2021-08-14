import os
import cv2
directory = 'sexy'  # directory you want to use
newDirectory = directory + '_cleaned'
desiredSize = 224

# https://jdhao.github.io/2017/11/06/resize-image-to-square-with-padding/
for filename in os.listdir(directory):
    print("-----------")
    if filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".jpg"):
        print(filename)
        image = cv2.imread(directory + "/" + filename)
        oldSize = image.shape[:2]  # oldSize is in (height, width) format
        ratio = float(desiredSize)/max(oldSize)
        newSize = tuple([int(x*ratio) for x in oldSize])
        # newSize should be in (width, height) format
        image = cv2.resize(image, (newSize[1], newSize[0]))

        deltaW = desiredSize - newSize[1]
        deltaH = desiredSize - newSize[0]
        top, bottom = deltaH//2, deltaH-(deltaH//2)
        left, right = deltaW//2, deltaW-(deltaW//2)

        color = [0, 0, 0]
        newImage = cv2.copyMakeBorder(
            image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

        cv2.imwrite(filename, newImage)
