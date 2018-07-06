# #6th July deep fashion meeting log
Because the dataset is too big to convert into tfrecord, the swp memory is full and the computer got frozen. 
→ Asked Brandon for help…. Other problems related to the dataset are discussed:

# 1. The dataset is organized poorly:
#####   (a)The classification is too specific, some clothing that are similar are classified into different categories. e.g. sweaters with neck and sweaters without neck are regarded as different classes. In total, there are 5612 folders, which means there are 5612 types of clothing. This is very difficult considering that ImageNet has only 1000 classes. Therefore, Brandon gave the advice that maybe we can extract a smaller number of classes to train the model instead of using the entire dataset. This may make it easier for the model to converge. 
#####   How the presentation will take form is also discussed: setup a camera and use our model to do detection. The model should be able to tell us what the person in the frame is wearing. So maybe a number of 30(upper clothing) + 30(lower clothing) + 30(full body) categories will suffice. Instead of 5612 classes.
##### (b)Some of the images have people in it: this will probably make the model confused. The model may misunderstand that the person in the image is an important feature of the clothing and cause misclassification.  

# 2. The ultimate goal:
#####   Brandon said that the ultimate goal is to construct a recommendation system that can first identify the style of the person according to what the person is wearing. Then recommend other pieces of clothing that the person may be interested in buying. But in order to do recommendations, detection must be done. So our goal is to first detect the clothing, since detection also gives us the information of what class the article of clothing it belongs to.)))))
