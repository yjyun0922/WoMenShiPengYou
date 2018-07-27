import os 

###the directory in which you have your img folder with only the images you want to keep 
PATH_TO_FILES = '/home/young-joo/Desktop/Cleaning_Complete/'

###the name of the bbox text file you just created using bbox_and_label.py
BBOX_FILE_OLD = 'bbox_full_body_wear.txt'
###what you want the name of the new bbox text file to be
BBOX_FILE_NEW = 'bbox_short_full_body_wear_filtered.txt'

###the name of the label text file you just create using 
LABEL_FILE_OLD = 'label_full_body_wear.txt'
###what you want the name of the new label text file to be 
LABEL_FILE_NEW = 'label_short_full_body_wear_filtered.txt'

#filter bbox file
our_file = open(PATH_TO_FILES + BBOX_FILE_OLD, 'r')
our_file = our_file.read().splitlines() 
donefile = open(PATH_TO_FILES + BBOX_FILE_NEW, "a+")
for our in our_file: 
	our_string = "".join(our)
	our_string = our_string.split()
	address = PATH_TO_FILES + our_string[0]
	if os.path.isfile(address) == True: 
		donefile.write(our + "\n") 
	else: 
		continue 
donefile.close()

#filter label file 
our_file = open(PATH_TO_FILES + LABEL_FILE_OLD, 'r')
our_file = our_file.read().splitlines()
donefile = open(PATH_TO_FILES + LABEL_FILE_NEW, "a+")
for our in our_file: 
	our_string = "".join(our)
	our_string = our_string.split()
	address = PATH_TO_FILES + our_string[0]
	if os.path.isfile(address) == True: 
		donefile.write(our + "\n")
	else: 
		continue  
