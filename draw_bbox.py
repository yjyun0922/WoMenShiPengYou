import os
import itertools 
import cv2 as cv
import numpy as np  
import tensorflow as tf
import matplotlib.pyplot as plt

PATH_TO_FILES = '/home/kelsonl/Desktop/test/'
TEXT_LOCATION_BBOX = PATH_TO_FILES + 'list_bbox.txt'

our_file = open(TEXT_LOCATION_BBOX, 'r')
our_file = our_file.readlines()
i = 1
for line in our_file:
	line = line.strip()
	line = line.split()
	image = cv.imread(PATH_TO_FILES + line[0])
	cv.rectangle(image, (int(line[1]),int(line[2])), (int(line[3]), int(line[4])), (0,0,255), 2)
	cv.imwrite(str(i) + '_bbox.jpg', image)
	i = i + 1