&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& HOW TO USE &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
FILL OUT THE PARAMETERS [YOU WILL SEE THE INSTRUCTION #FILL THIS OUT#] 
//save_to_tfrecord.py//
	TEXT_LOCATION_LABEL (path to the file containing a list of images and their addresses)
	TEXT_LOCATION_BBOX (path to the file containing a list of path to images and their bounding box coordinates)
	TEXT_LOCATION_CAT (path to the file containing a list of integer labels and their corresponding string names)
	TFRECORD_NAME (the name of the TFRecord file that will be produced) 
//read_tfrecord.py//
	record (the name of the TFRecord file that will be read)
	BATCH_SIZE (the number of images you want to see each time)
	NUM_BATCH (the number of batches you want to get)

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& TOPICS &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(1) Checklist 
(2) Why TFRecord?   
(3) Save_to_TFRecord.py
(4) Read_TFRecord.py 
(5) Citations 

&&&&&&&&&&&&&&&&&&&&&&&&&&&&& (1) CHECKLIST &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(%) Make sure you have opened this README.md file with Sublime Text 
(%) Your images are in the format of jpg 
(%) You have the three text files mentioned in the <HOW TO USE> section

&&&&&&&&&&&&&&&&&&&&&&&&&&& (2) WHY TFRECORD? &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(%) Can organize and keep track of your data easily 
(%) Very compatible with TensorFlow  
(%) The format used by Tensorflow Object Detection API

&&&&&&&&&&&&&&&&&&&&&&&& (3) SAVE_TO_TFRECORD.PY &&&&&&&&&&&&&&&&&&&&&&&&&&
(%) //purpose//
	Saves your data to a TFRecord file 
(%) //function: label_list()//
	//function: bbox_list()//
	//function: cat_list()//
	Reads information from your text files and stores them in the form of lists
(%) //function: int64_feature()//
	//function: bytes_feature()//
	//function: float_list_feature()//
	Helper functions that convert the data in our lists to the type of Feature because Feautures are the components of Examples, the arrays of which form a TFRecord file. These functions are from the official TensorFlow GitHub Repo. 
(%) //function: save_to_record()//
	Using the helper functions mentioned above, converts our data and stores them in the type of Feature to Example, which we then write to TFRecord. We repeat this process for each of our image.  

&&&&&&&&&&&&&&&&&&&&&&&&&& (4) READ_TFRECORD.PY &&&&&&&&&&&&&&&&&&&&&&&&&&&
(%) //purpose//
	Reads your TFRecord file and returns batches of images as outputs
(%) //function: read_and_decode()//
	shuffles the data in TFRecord to randomize the output, reads the shuffled file, and extracts the information that is necessary to reconstruct the images. Then, creates batches of images. 
(%) //function: plot_images()//
	Visualizes the reconstructed images 
(%) //running TensorFlow session// 
	Opens a new session, enabling us to actually create the batches of images and plot them. 

&&&&&&&&&&&&&&&&&&&&&&&&&&&&& (5) CITATIONS &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(%) https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/5_DataManagement/build_an_image_dataset.py
    (explains how to read from text files)
(%) https://towardsdatascience.com/how-to-train-your-own-object-detector-with-tensorflows-object-detector-api-bec72ecfe1d9
    (really helpful explanation of object detection)
(%) https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md
    (a detailed list of the Features contained in the Example, especially for object detection)
    (official instruction written by TensorFlow developers)
(%) https://stackoverflow.com/questions/49986522/read-data-from-tfrecord-file-used-in-object-detection-api
    (really helpful step-by-step guide on saving to TFRecord and reading TFRecord for object detection)
(%) http://machinelearninguru.com/deep_learning/tensorflow/basics/tfrecord/tfrecord.html
	(good explanation of saving to TFRecord and reading TFRecord)
	(good explanation of the concepts of protocal buffer, examples, features, and serialization)
	(not specifically for object detection)# WoMenShiPengYou
