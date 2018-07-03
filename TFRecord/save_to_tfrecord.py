import os
import itertools 
import cv2 as cv
import numpy as np  
import tensorflow as tf

#FILL THIS OUT# 
TEXT_LOCATION_LABEL = '/home/yjyun0922/Desktop/obj_detection/short_cat.txt' 
TEXT_LOCATION_BBOX = '/home/yjyun0922/Desktop/obj_detection/short_bbox.txt'
TEXT_LOCATION_CAT = '/home/yjyun0922/Desktop/obj_detection/list_category_cloth.txt'
TFRECORD_NAME = 'tfrecord_is_great'

def label_list(text_location_label): 
	images_addr = list()
	labels = list()
	files_name = list()
	our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()
	for our in itertools.islice(our_file, 2, None):  
		our_string = "".join(our)
		our_string = our_string.split()
		images_addr.append(our_string[0])
		labels.append(int(our_string[1]))
		file_name = '/home/yjyun0922/Desktop/obj_detection/' + our_string[0]
		files_name.append(file_name)
	return images_addr, labels, files_name 

def bbox_list(text_location_bbox): 
	images = list()
	heights = list()
	widths = list()
	dims = (heights, widths)
	xmins = list() 
	xmaxs = list()
	ymins = list()
	ymaxs = list()
	bboxs = (xmins, xmaxs, ymins, ymaxs) 
	our_file = open(text_location_bbox, 'r')
	our_file = our_file.read().splitlines()
	for our in itertools.islice(our_file, 2, None): 
		our_string = "".join(our)
		our_string = our_string.split() 
		address = our_string[0]
		image = cv.imread('/home/yjyun0922/Desktop/obj_detection/' + address)
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		(h, w) = image.shape[:2]
		images.append(image)
		heights.append(h)
		widths.append(w)
		xmin_before = int(our_string[1])
		xmax_before = int(our_string[3])
		ymin_before = int(our_string[2])
		ymax_before = int(our_string[4])
		xmin_normalized = xmin_before / w
		xmax_normalized = xmax_before / w
		ymin_normalized = ymin_before / h
		ymax_normalized = ymax_before / h
		xmins.append(xmin_normalized)
		xmaxs.append(xmax_normalized)
		ymins.append(ymin_normalized)
		ymaxs.append(ymax_normalized) 
	return images, dims, bboxs 

def cat_list(text_location_cat): 
	cats = list()
	our_file = open(text_location_cat, 'r')
	our_file = our_file.read().splitlines()
	for our in itertools.islice(our_file, 2, None): 
		our_string = "".join(our)
		our_string = our_string.split()
		cats.append(our_string[0])
	return cats

def int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
def bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
def float_list_feature(value):
  return tf.train.Feature(float_list=tf.train.FloatList(value=value))

def save_to_record(images_addr, labels, files_name, images, dims, bboxs, cats): 
	filename = TFRECORD_NAME 
	writer = tf.python_io.TFRecordWriter(filename)
	if len(images_addr) != len(images): 
		raise Exception("Error: the lengths are different.") 
	length = len(images_addr) 
	for i in range(length):
		label_num = labels[i]
		example = tf.train.Example(features=tf.train.Features(feature={
			'image/height': int64_feature(dims[0][i]),
  			'image/width': int64_feature(dims[1][i]),
  			'image/filename': bytes_feature(files_name[i].encode()),
  			'image/source_id': bytes_feature(files_name[i].encode()),
  			'image/encoded': bytes_feature(images[i].tostring()),
  			'image/format': bytes_feature(b'jpg'),
      		'image/object/bbox/xmin': float_list_feature([bboxs[0][i]]),
      		'image/object/bbox/xmax': float_list_feature([bboxs[1][i]]),
      		'image/object/bbox/ymin': float_list_feature([bboxs[2][i]]),
      		'image/object/bbox/ymax': float_list_feature([bboxs[3][i]]),
      		'image/object/class/text': bytes_feature(cats[label_num].encode()),
      		'image/object/class/label': int64_feature(labels[i])
		}))
		writer.write(example.SerializeToString())
	writer.close()
	return example 

images_addr, labels, files_name = label_list(TEXT_LOCATION_LABEL)
images, dims, bboxs = bbox_list(TEXT_LOCATION_BBOX)
cats = cat_list(TEXT_LOCATION_CAT)
example = save_to_record(images_addr, labels, files_name, images, dims, bboxs, cats)
print "Test Successful"
