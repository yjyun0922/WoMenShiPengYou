Our Decision Making Process Regarding the Type of Transfer Learning to Use 

#####Important Factors to Consider
Factor 1: size of the new dataset
Factor 2: similarity to the original dataset

#####Our Case
Factor 1 is not under our control. 
Factor 2 is under our control. 
Therefore, we have two different options: 
Option 1: large dataset & similar to the original dataset
	- less worried about overfitting
	- can fine-tune some higher-level portion of the CNN
Option 2: large dataset & different from the original dataset
	- can afford to train CNN from scratch 
	- still, try to initialize with weights froma pretrained model 
	- fine-tune through the entire network 

#####Conclusion
Two possibilities: 
Possibility 1: fine-tune the pre-trained CNN partially
Possibility 2: fine-tune the pre-trained CNN entirely while initializing with weights from the pre-trained model 

We could initially try four different experiments: 
(Open-image, possibility 1)
(Open-image, possibility 2)
(COCO, possibility 1) 
(COCO, possibility 2)

Comment 1: I think the Kaggle article uses COCO because COCO has many more pre-trained models - possibiltiy because Open-Images is super big and therefore takes much more time to train on it  

Comment 2: If we have the time, we could try varying the original data set while keeping the model the same to see the effect on the similirity to the orignial dataset on model performance: 
- Models only trained on COCO: for each model, try only on COCO while varying the tuning process 
	- ssd mobilenet v1 
	- ssd mobilenet v2
	- ssdlite mobilenet v2
	- ssd inception v2
	- faster rcnn inception v2
	- faster rcnn resnet50
	- faster rcnn resnet50 lowproposals 
	- rfcn resnet101
	- faster rcnn resnet101 lowproposals
	- faster rcnn nas
	- faster rcnn nas lowproposals 
	- mask rcnn inception resnet v2 atrous
	- mask rcnn inception v2
	- mask rcnn resnet101 atrous
	- mask rcnn resnet50 atrous  
- Models trained on all COCO and Kitti and AVA: for each model, try on all three while varying the tuning process
	- faster rcnn resnet101
- Models trained on COCO and Open Images: for each model, try on both while varying the tuning process 
	- faster rcnn inception resnet v2 atrous 
	- faster rcnn inception resnet vs atrous lowproposals  


#####What to Keep in Mind
- cannot arbitrarily take out Conv layers from the pretrained network 
- can change the spatial size of the images b/c the layers are independent of image sizes
- use a smaller learning rate for ConvNet weights that are being fine-tuned b/c we expect that the ConvNet weights are good, so we don't want to distort them too quickly and too much
