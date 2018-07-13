import os
import itertools 
import cv2 as cv
import numpy as np  
import PIL 
from PIL import Image 

#PLEASE HAVE ALL THE FILES YOU NEED TOGETHER IN ONE FILE# 
#FILL IN THE PATH TO THE FOLDER THAT CONTAINS ALL OF YOUR FILES#
PATH_TO_FILES = '/home/young-joo/Desktop/obj_detection/'
 
#YOU DON'T NEED TO CHANGE ANY OF THIS 
TEXT_LOCATION_LABEL = PATH_TO_FILES + 'list_category_img.txt' 

def convert_image(text_location_label): 
	images_addr = list()
	our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()
	for our in itertools.islice(our_file, 2, None):  
		our_string = "".join(our)
		our_string = our_string.split()
		images_addr.append(our_string[0])
		length = len(images_addr)
	for i in range(length):
		split = images_addr[i].split(".")
		img = Image.open(PATH_TO_FILES + images_addr[i]) 
		img = img.resize((299, 299), PIL.Image.ANTIALIAS) 
		img.save(PATH_TO_FILES + split[0] + "revised.jpg")
		print "converted %d out of %d images" % (i, length)

convert_image(TEXT_LOCATION_LABEL)

