import os 
import cv2 as cv
import random 
import numpy as np 
import tensorflow as tf
import matplotlib.pyplot as plt 

shuffle_data = True

PATH_TO_FILES = '/home/young-joo/Desktop/Dataset/'
JUMPSUIT = PATH_TO_FILES + 'bbox_Jumpsuit.txt'
DRESS = PATH_TO_FILES + 'bbox_Dress.txt'

#Save into a list 
def return_lists(JUMPSUIT, DRESS): 
	jump_file = open(JUMPSUIT, 'r').read().splitlines()
	dress_file = open(DRESS, 'r').read().splitlines()
	our_file = jump_file + dress_file ##do sth about this LINE 
	#[0]: addr [1]: bbox [2]: string-name [3]: label
	
	our_list = []

	our_list.append([])
	our_list.append([])
	our_list.append([])
	our_list.append([])
	
	length = len(our_file)
	for our in range(length):
		our_string = "".join(our_file[our])
		our_string = our_string.split() 
		
		addr = our_string[0]
		our_list[0].append(addr)		
	
		xmin = float(our_string[1])
		xmax = float(our_string[2])
		ymin = float(our_string[3])
		ymax = float(our_string[4])
		bbox = (xmin, xmax, ymin, ymax)  
		our_list[1].append(bbox)
 
		if 'Jumpsuit' in addr: 
			category = 'Jumpsuit'
			our_list[2].append(category)
			label = 1
			our_list[3].append(label)
		elif 'Dress' in addr: 
			category = 'Dress'
			our_list[2].append(category)
			label = 2
			our_list[3].append(label)
		else: 
			raise ValueError('Something is wrong') 
	return our_list 

this_is_the_list = return_lists(JUMPSUIT, DRESS)

print this_is_the_list[0][0]
print this_is_the_list[1][0]
print this_is_the_list[2][0]
print this_is_the_list[3][0]

print this_is_the_list[0][1999]
print this_is_the_list[1][1999]
print this_is_the_list[2][1999]
print this_is_the_list[3][1999]

addrs = this_is_the_list[0]
bboxs = this_is_the_list[1]
string_names = this_is_the_list[2]
labels = this_is_the_list[3]

if shuffle_data: 
	c = list(zip(addrs, bboxs, string_names, labels))
	random.shuffle(c)
	addrs, bboxs, string_names, labels = zip(*c)
 
print addrs[0]
print bboxs[0]
print string_names[0]
print labels[0]

print addrs[1999]
print bboxs[1999]
print string_names[1999]
print labels[1999]

#Divide into train and test sets
train_addrs = addrs[0:int(0.8*len(addrs))]
train_bboxs = bboxs[0:int(0.8*len(bboxs))]
train_string_names = string_names[0:int(0.8*len(string_names))]
train_labels = labels[0:int(0.8*len(labels))]

test_addrs = addrs[int(0.8*len(addrs)):]
test_bboxs = bboxs[int(0.8*len(bboxs)):]
test_string_names = string_names[int(0.8*len(string_names)):]
test_labels = labels[int(0.8*len(labels)):]

#Helper functions for converting data types 
def int64_feature(value): 
	return tf.train.Feature(int64_list = tf.train.Int64List(value = [value]))
def bytes_feature(value): 
	return tf.train.Feature(bytes_list = tf.train.BytesList(value = [value]))
def float_list_feature(value): 
	return tf.train.Feature(float_list = tf.train.FloatList(value = value))
		
#Saving to tfrecord
def save_to_record(filename, addrs_addrs, bboxs_bboxs, string_string, labels_labels): 
	writer = tf.python_io.TFRecordWriter(filename)
	length = len(addrs_addrs)
	count = 0
	print "this is the original length: %d" % (length) 
	for i in range(length):  
		if count % 100 == 0: 
			print length
			print("%d out of %d saved" % (count, length))
		image = cv.imread(PATH_TO_FILES + addrs_addrs[i])
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		(h, w) = image.shape[:2]
		split = addrs_addrs[i].split(".")
		with tf.gfile.GFile(PATH_TO_FILES + split[0] + "_revised.jpg", 'rb') as fid: 
			encoded_jpg = fid.read()
			label_num = labels_labels[i] 
			example = tf.train.Example(features = tf.train.Features(feature = { 
			'image/height': int64_feature(299),
			'image/width': int64_feature(299), 
			'image/encoded': bytes_feature(encoded_jpg), 
			'image/format': bytes_feature(b'jpg'), 
			'image/object/bbox/xmin': float_list_feature([bboxs_bboxs[i][0] / w]), 
			'image/object/bbox/xmax': float_list_feature([bboxs_bboxs[i][1] / w]), 
			'image/object/bbox/ymin': float_list_feature([bboxs_bboxs[i][2] / h]), 
			'image/object/bbox/ymax': float_list_feature([bboxs_bboxs[i][3] / h]), 
			'image/object/class/text': bytes_feature(string_string[label_num].encode()), 
			'image/object/class/label': int64_feature(label_num)
			}))
		count = count + 1
		writer.write(example.SerializeToString())
	writer.close()
	return example 

if __name__ == '__main__': 
	#Generating training data
	save_to_record('train', train_addrs, train_bboxs, train_string_names, train_labels)
	#Generating testing data
	save_to_record('test', test_addrs, test_bboxs, test_string_names, test_labels) 
















	
