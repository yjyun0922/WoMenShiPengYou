import os 

###the directory in which you have the very original label and bbox text files 
PATH_TO_FILES = '/home/young-joo/Desktop/Programs_for_Cleaning_Data/'
###what you want the name of the generated bbox file to be 
BBOX_NAME = 'bbox_full_body_wear.txt'
###what you want the name of the generated label file to be
LABEL_NAME = 'label_full_body_wear.txt'

###The category you want to find 
WHAT_TO_FIND = "Dress"
###The corresponding label number
LABEL_NUM = "10"

#creates the label file 
our_file = open(PATH_TO_FILES + "list_category_img.txt", 'r')
our_file = our_file.read().splitlines()
donefile = open(PATH_TO_FILES + LABEL_NAME, "w")
for our in our_file: 
	our_string = "".join(our)
	our_string = our_string.split()
	address = PATH_TO_FILES + our_string[0]
	if "_" + WHAT_TO_FIND in address: 
		donefile.write(our_string[0] + " " + LABEL_NUM + "\n")
	else: 
		continue 
donefile.close()

#creates the bbox file 
our_file = open(PATH_TO_FILES + "list_bbox.txt", 'r')
our_file = our_file.read().splitlines()
donefile = open(PATH_TO_FILES + BBOX_NAME, "w")
for our in our_file: 
	our_string = "".join(our)
	our_string = our_string.split()
	address = PATH_TO_FILES + our_string[0]
	if "_" + WHAT_TO_FIND in address: 
		donefile.write(our + "\n")
	else: 
		continue 
donefile.close()  
