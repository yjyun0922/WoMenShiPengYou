#### Article that introduces Transfer learning -- CS231n
###### http://cs231n.github.io/transfer-learning/
#### Github repository of tensorflow object detection 
###### https://github.com/tensorflow/models/tree/master/research/object_detection
#### Introduction to the model zoo of object detection models
###### https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
###### there are 4 categories of models: models trained on (1) COCO (2) Kitti (3) Open-image (4) AVA 
###### (1) COCO is a dataset with 330K images & 80 object categories. 
###### http://cocodataset.org/#home
###### (2) Kitti is a dataset about road view 
###### http://www.cvlibs.net/datasets/kitti/eval_tracking.php
###### (3) Open-image is an extremely huge and new dataset with 9 million images & 600 categories
###### https://storage.googleapis.com/openimages/web/index.html
###### (4) AVA is a dataset that annotates 80 atomic visual actions in 430 15-minute movie clips
######  https://research.google.com/ava/ 

###### We have to choose which model to use for our dataset to do transfer learning. From this article, https://www.kaggle.com/shivamb/imaterialist-fashion-eda-object-detection-colors/notebook, I see that they have a smaller dataset and transfers from models trained on COCO. So I figure we could also use models  pretrained on COCO.
