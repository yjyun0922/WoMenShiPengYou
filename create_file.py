import random
import os
import itertools 
import cv2 as cv
import numpy as np  
import PIL 
from PIL import Image 


PATH_TO_FILES = '/home/kelsonl/Desktop/Dataset/'
what_to_find = ["Shorts", "Jeans", "Joggers"]

def create_list(text_location_label, keyword): 
	our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()
	our_list = []
	i = 1
	for our in our_file[2:]:   
		our_string = "".join(our)
		our_string = our_string.split()
		address = our_string[0]
		address_split = address.split("/")
		name = address_split[1]
		name_split = name.split("_")
		category = name_split[-1]
		if keyword == category:
			print "%d" % i
			our_list.append(our)
			i += 1
		else: 
			continue
	return our_list

def rename_image(bbox_list, keyword): 
	our_list = bbox_list
	new_list = []
	i = 1
	for our in our_list:   
		string = our
		our_string = string.split()
		address = PATH_TO_FILES + our_string[0] 
		if os.path.isfile(address) == True:
			print "%d" % i 
			new_list.append((keyword+"/%d.jpg " % (i)) + "\n")
			i += 1
		else: 
			continue
	return new_list

def rename_image2(bbox_list, keyword): 
	our_list = bbox_list
	new_list = []
	i = 1
	for our in our_list:   
		string = our
		our_string = string.split()
		address = PATH_TO_FILES + our_string[0] 
		if os.path.isfile(address) == True:
			print "%d" % i 
			new_list.append((keyword+"/%d.jpg " % (i)) + our_string[1] +  " " + our_string[2] + " " + our_string[3] + " " +  our_string[4] + "\n")
			i += 1
		else: 
			continue
	return new_list


def get_1000(bbox_list):
	our_list = bbox_list
	new_list = []
	count = 1
	for i in range(len(our_list)):
		new_list.append(our_list[i])
		count = count + 1
		if count > 1000:
			break
	return new_list

def distribute(the_list):
	our_list = the_list
	new_list = []
	count = 0
	for i in range(len(our_list)):
		string = our_list[i].strip()
		count = count + 1
		if count < 801:
			string = string + "\ttrain\n"
		else:
			string = string + "\ttest\n"
		new_list.append(string)
	return new_list

def get_num(line):
	new_line = line
	new_line = new_line.strip()
	new_line = new_line.split()
	new_line = new_line[0]
	new_line = new_line.split("/")
	new_line = new_line[1]
	new_line = new_line.split(".")
	new_line = new_line[0]
	return int(new_line)

def get_list(keyword):
	bbox_list = create_list(PATH_TO_FILES+"bbox_list.txt", keyword)
	bbox_list = rename_image(bbox_list, keyword)
	our_list = get_1000(bbox_list)
	random.shuffle(our_list)
	our_list = distribute(our_list)
	our_list.sort(key=get_num)
	return our_list

def get_list2(keyword):
	bbox_list = create_list(PATH_TO_FILES+"bbox_list.txt", keyword)
	bbox_list = rename_image2(bbox_list, keyword)
	our_list = get_1000(bbox_list)
	return our_list

our_list = []

for keyword in what_to_find:
	our_list.extend(get_list(keyword))

new_file = open('list_eval.txt','w')
for line in our_list:
	new_file.write(line)
new_file.close()

our_list2 = []

for keyword in what_to_find:
	our_list2.extend(get_list2(keyword))

new_file2 = open('list_bbox.txt','w')
for line in our_list2:
	new_file2.write(line)
new_file2.close()