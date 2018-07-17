import os
import itertools 
import cv2 as cv
import numpy as np  
import PIL 
from PIL import Image 


PATH_TO_FILES = '/home/kelsonl/Desktop/Dataset/'
what_to_find = "Chinos"
TEXT_LOCATION_LABEL = PATH_TO_FILES + 'bbox_list.txt' 

def create_list(text_location_label, keyword): 
	our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()
	donefile = open(PATH_TO_FILES + "original.txt", "w")
	i = 1
	for our in our_file:   
		our_string = "".join(our)
		our_string = our_string.split()
		address = PATH_TO_FILES + our_string[0] 
		if "_"+keyword in address:
			print "%d" % i
			donefile.write(our+"\n")
			i += 1
		else: 
			continue
	donefile.close()	
create_list(TEXT_LOCATION_LABEL, what_to_find)
