I showed Brandon my configuration file as well as the graphs for the total loss. 
Observation: too many fluctuations in the loss function for unknown reasons
Problem: 50 is a huge number of categories 
Possible solution: change the number of categories to around 20 
Reasoning: The model was originally trained on the COCO dataset, which consists of images that are very distinct. 
For example, trees, humans, animals, and food are all very different objects. On the other hand, all of the images
in our dataset are those of clothing articles. Therefore, we should at least narrow down the number of categories to eliminate
clothes that are too similar. 

How to approach the process of training:
It's like a decision tree diagram. 
- Make one change, and see what happens 
- Depending on the result, make other changes
MAKE ONE CHANGE AT A TIME = change only one thing in the configuration file each time

Brandon said that what we are encountering is a common problem in machine learning, so it's ok!! We're doing great!! 

FYI: 
I started reading the deep learning book by Ian Goodfellow, and I asked which parts were relevant to our work: 
Brandon said chapter 8, chapter 9, and chapter 12.2, just in case anyone is curious!! 

What I think we should do now: 
- decide as a team on which 20-ish categories to keep 
--- The way of changing our save_to_tfrecord.py file should be simple
--- instead of making big changes, we could just make a conditional statement that says
--- "if the original number (the label we have right now) is 50, 49, or 47, then change the label number to 19"
- maybe create a shared PowerPoint or Excel to store the screenshots of our results (for each model) 
so that we have good documentation of what we have done so far, which will enable us to compare it to 
the results we will get in the future and analyze them together. 
- Also, the process of making changes to improve the model is more important than just getting the results because 
then we know why our model is behaving in a certain way. 
