## 12th July deep fashion meeting log 
One of our models was still in the process of being trained (even after the typhoon), and two of our models were done with training. We had a group meeting so that we could discuss what we should do next, in terms of using the validation dataset. Other problems and possible solutions were discussed as well: 

# 1. Using validation data set to decreases losses: 
##### if the computer can manage to train and evaluate at the same time: 
Towards the end of the training, when the losses seem to have stabilized, try tweaking certain parameters that could potentially decrease the loss. If the loss either increases or doesn't get decreased, then try tweaking a different parameter. If the loss decreases, keep training using that parameter until the loss stabilizes again. Repeat these steps with different parameters until you can't decrease the loss anymore. 
##### if the computer can't manage to train and evaluate at the same time: 
We won't be able to automatically change the parameters and feed in the new configuration file to the running model, so we'll have to kill the training process after we get a checkpoint file. The results should be the same as above, so this is not too much of a concern. 
##### regarding the learning rate: 
We need to decrease it as the accuracy increases. We can either do this manually or use Adam, but since using Adam would be more accurate and more time efficient, Adam would be prefered. Depending on whether we can use Adam or not, the loss would stabilize around a certain value while fluctuating (without Adam) or stop decreasing or changing after a certain vale (with Adam). Using Adam would reduce human error.  

# 2. Short-term goal 
(a) do research on Adam and see how we can implement it to our model
(b) do research on the different parameters we can tweak
After doing this research, we will decide what direction to take in the future. 
--------------
#Update after the meeting: 
##### problem: we checked the partial results of running evaluation. object detection seems to work decently, but image classification performance was really poor. The evaluation process also took a really long time. 
##### solution: we thought that maybe classifying images into 50 categories was too hard of a task for our models. Therefore, we decided to first have our model classify our dataset into three different categories: top, bottom, and dresses. We still have the same goals in mind (tweaking parameters to reduce the loss and possibly using Adam), but we are only going to have three different categories. 
##### what to do now: 
(1) do research on Adam and see how it can be implemented in our models - Young-Joo
(2) do research on the different parameters we can tweak for each model - Wayne 
(3) refactor the tfrecord files so that we only have three categories - Kelson 






 
