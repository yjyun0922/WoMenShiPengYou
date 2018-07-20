import os
import itertools 
import cv2 as cv
import numpy as np  
import PIL 
from PIL import Image 

#PLEASE HAVE ALL THE FILES YOU NEED TOGETHER IN ONE FILE# 
#FILL IN THE PATH TO THE FOLDER THAT CONTAINS ALL OF YOUR FILES#
PATH_TO_FILES = '/home/young-joo/Desktop/Dataset/'
 
#YOU DON'T NEED TO CHANGE ANY OF THIS 
JUMPSUIT = PATH_TO_FILES + 'bbox_Jumpsuit.txt'
DRESS = PATH_TO_FILES + 'bbox_Dress.txt' 

def convert_image(my_file): 
	addrs = list()
	our_file = open(my_file, 'r')
	our_file = our_file.read().splitlines()
	length = len(our_file) 
	for our in range(length):   
		our_string = "".join(our_file[our])
		our_string = our_string.split()
		addrs.append(our_string[0])
	for i in range(length):
		split = addrs[i].split(".")
		img = Image.open(PATH_TO_FILES + addrs[i]) 
		img = img.resize((299, 299), PIL.Image.ANTIALIAS) 
		img.save(PATH_TO_FILES + split[0] + "_revised.jpg")
		print "converted %d out of %d images" % (i + 1, length)

convert_image(JUMPSUIT)
convert_image(DRESS) 

