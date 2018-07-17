import os
import itertools 
import cv2 as cv
import numpy as np  
import PIL 
from PIL import Image 

#Prerequisite:
#The folder in which you deleted images should be contained inside a folder caled img
#in the same directory as the one img is in, create text file called original.txt
#in which you can copy and paste the chunk in list_bbox corresponding to your folder
#in the same directory, create another file called donefile.txt
#Now, you can run the file
#When the images are generated and donefile.txt gets filled up, 
#You can copy and paste the images to your folder where you're storing images, 
#and you can also copy and paste what you have in your donefile to the file where you're keeping track of the bounded boxes for theiamges in your folder

#PLEASE HAVE ALL THE FILES YOU NEED TOGETHER IN ONE FILE# 
#FILL IN THE PATH TO THE FOLDER THAT CONTAINS ALL OF YOUR FILES#
PATH_TO_FILES = '/home/young-joo/Desktop/Dataset/'
 
#YOU DON'T NEED TO CHANGE ANY OF THIS 
TEXT_LOCATION_LABEL = PATH_TO_FILES + 'original.txt' 

def rename_image(text_location_label): 
	our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()
	donefile = open(PATH_TO_FILES + "donefile.txt", "a+")
	i = 136
	for our in our_file:   
		our_string = "".join(our)
		our_string = our_string.split()
		address = PATH_TO_FILES + our_string[0] 
		if os.path.isfile(address) == True:
			print "%d" % i 
			img = Image.open(address)
			img.save("%d.jpg" % i)
			donefile.write(("Coat/%d.jpg " % (i)) + our_string[1] +  " " + our_string[2] + " " + our_string[3] + " " +  our_string[4] + "\n")
			i += 1
		else: 
			continue  
	donefile.close()	
rename_image(TEXT_LOCATION_LABEL)

