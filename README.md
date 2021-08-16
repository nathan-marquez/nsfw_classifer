This repo is based off of and modifies the work done by GantMan here: https://github.com/GantMan/nsfw_model


Tested with and currently requires: 
Python 3.83
Tensorflow 2.6.0
Keras 2.6.0


Finding and cleaning data:
Images can be scraped using RipMe from different subreddits. 
You can then use the cleaning script included to resize the data to fit the desired input size. 
For mobilenetv2, this is 224x224. The script is a little crude, as of now it just pulls from a folder within the same directory as the script and then saves the images within that directory. So if you have a "sexy" folder, it should include clean.py and a subfolder with the precleaned images. Running the script will then populate the sexy folder.


Training:
Training data should be placed in the images folder, and should be separated into each of the five subfolders based on their true label (drawings, hentai, neutral, porn, and sexy). 

When ready to train, you can run the train_all_models script (either the .cmd or .sh). If you have no models in the trained_models folder, then the scripts will automatically download new models and train them. Models already in the folder will undergo training again. You can comment out the models in the script that you don't want to train, and you can also change the number of epochs in the script that you want to run.

Currently, the trained_models folder contians the originally trained MobileNetV2 by GantMan (mobilenet_v2_140_224_og), the model I trained (mobilenet_v2_140_224) to better differentiate between borderline NSFW content (Thirst Traps, Bikini Pics) and true NSFW content, as well as the model that is ready to be used on the web with tensorflowjs (mobilenet_v2_140_224_js). The next section will describe how to convert the model to work with tensorflowjs, which is what is necessary for this model to work with NSFWJS.



Testing and generating confusion matrices:
To individually test images with your model, you can run

python3 nsfw_detector/predict.py --saved_model_path trained_models/mobilenet_v2_140_224 --image_dir images/hentai/example.jpg

To generate confusion matrices, you can use the visuals.py script.




Deploying the model:

To deploy the model on web, install tensorflowjs with pip install tensorflowjs. This will overide some files in the normal tensorflow, so be warned that once you do this you will have to reinstall normal tensorflow in order to retrain your model. 

Then, in the trian_all_models script, comment out the lines to train the models and uncomment the lines directly below to convert your model to work with tensorflowjs.

Once this is done, the model within the trained_models folder will have a web_model folder with shards that can be uploaded to your site. NSFWJS can then load these files by passing the absolute URL of the directory of the shards and model.json into nsfwjs.load("path/to/model")

Note that in the conversion script, we convert to a graph model, so when loading into nsfwjs, it is import to include: 

const model = await nsfw.load("file://path/to/model", {
  type: "graph",
});
