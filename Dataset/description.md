#This is a description about our dataset

##How it's organized 
- folders containing images belonging to the same category
- a text file that matches each string label to a integer label
- a text file that contains the path to the imgages, their corresponding numbered labels, and their corresponding bouning box coordinates (x1, y1, x2, y2)

##How they have been categorized
- it is how it looks like: if it looks like a dress, it is a dress, if it looks like pants, it is pants. Someone who wears a romper wears it because he/she/they want(s) the other person to think he/she/they is/are wearing a dress. Therefore, no matter what it ACTUALLY is, we will categorize it based on HOW IT LOOKS LIKE
 
####Below is our definition of each category 
- Dress: a long piece of clothes that has the top and bottom connected, with the bottom part resembling a skirt. (note: if a dress looks like the top and bottom part are separate, the bottom part will be categorized as a skirt instead of a dress) 




##Purpose and consequences
- We want our model to be able to tell what a person in a picture is wearing. Therefore, we are going to only have images that have people in them. 
