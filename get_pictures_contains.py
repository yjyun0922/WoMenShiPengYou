import os
import itertools 
import cv2 as cv
import numpy as np  
import PIL 
from PIL import Image 
import matplotlib.pyplot as plt 
from scipy import misc
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
PATH_TO_FILES = '/home/waynelin/Desktop/fashion/data/'
what_to_find = "Tee"
 
#YOU DON'T NEED TO CHANGE ANY OF THIS 
TEXT_LOCATION_LABEL = PATH_TO_FILES + 'list_bbox.txt'
TEXT_LOCATION_LABEL2 = PATH_TO_FILES + 'original.txt'

def create_list(text_location_label, keyword): 
	our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()
	donefile = open(PATH_TO_FILES + "original.txt", "w+")
	i = 1
	for our in our_file[2:]:   
		our_string = "".join(our)
		our_string = our_string.split()
		address = our_string[0]
		if "_"+keyword in address:
			print "%d" % i
			donefile.write(our+"\n")
			i += 1
		else: 
			continue
	donefile.close()

def rename_image(text_location_label, keyword): 
	our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()
	donefile = open(PATH_TO_FILES + "donefile.txt", "a+")
	i = 1
	for our in our_file:   
		our_string = "".join(our)
		our_string = our_string.split()
		address = PATH_TO_FILES + our_string[0] 
		if os.path.isfile(address) == True:
			print "%d" % i 
			img = Image.open(address)
			img.save("%d.jpg" % i)
			donefile.write((keyword+"/%d.jpg " % (i)) + our_string[1] +  " " + our_string[2] + " " + our_string[3] + " " +  our_string[4] + "\n")
			i += 1
		else: 
			continue
	donefile.close()	
def visualizeBB(text_location_label):
    our_file = open(text_location_label, 'r')
    our_file = our_file.read().splitlines()
    for our in our_file:
        our_string ="".join(our)
        our_string = our_string.split()
        address = PATH_TO_FILES + our_string[0]
        print address
        if os.path.isfile(address) == True:
            x1 = int(our_string[1])
            x2 = int(our_string[3])
            y1 = int(our_string[2])
            y2 = int(our_string[4])
            x1 -=1
            x2 -=1
            y1 -=1
            y2 -=1
            print x1, x2, y1, y2
            f = misc.imread(address)
            f[y1:y1+3,x1:x2,0] = 255
            f[y1:y1+3,x1:x2,1] = 0
            f[y1:y1+3,x1:x2,2] = 0
            
            f[y2-3:y2,x1:x2,0] = 255
            f[y2-3:y2,x1:x2,1] = 0
            f[y2-3:y2,x1:x2,2] = 0
            
            f[y1:y2,x1:x1+3,0] = 255
            f[y1:y2,x1:x1+3,1] = 0
            f[y1:y2,x1:x1+3,2] = 0
            
            f[y1:y2,x2-3:x2,0] = 255
            f[y1:y2,x2-3:x2,1] = 0
            f[y1:y2,x2-3:x2,2] = 0
            plt.imshow(f)
            plt.show()
        else:
            print "file doesn't exist"
#create_list(TEXT_LOCATION_LABEL, what_to_find)
#rename_image(TEXT_LOCATION_LABEL2, what_to_find)
visualizeBB(TEXT_LOCATION_LABEL)
