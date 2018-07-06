import os
import itertools 
import cv2 as cv
import numpy as np  
import tensorflow as tf

#FILL THIS OUT# 
TEXT_LOCATION_LABEL = '/home/kelsonl/Desktop/obj_detection/short_cat.txt' 
TEXT_LOCATION_BBOX = '/home/kelsonl/Desktop/obj_detection/short_bbox.txt'
TEXT_LOCATION_CAT = '/home/kelsonl/Desktop/obj_detection/list_category_cloth.txt'
TFRECORD_NAME = 'tfrecord_is_great'

def new_label_list(text_location_label, text_location_cat):
	our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()

	cat1 = []
	cat2 = []
	cat3 = []
	cat1.append([])
	cat1.append([])
	cat1.append([])
	cat2.append([])
	cat2.append([])
	cat2.append([])
	cat3.append([])
	cat3.append([])
	cat3.append([])

	for our in our_file[2:]:
		our_string = "".join(our)
		our_string = our_string.split()
		image_address = our_string[0]
		label = our_string[1]
		file_name = '/home/kelsonl/Desktop/obj_detection/' + image_address
		cat = get_cat(image_address, text_location_cat)
		if cat == '1':
			cat1[0].append(image_address)
			cat1[1].append(int(label))
			cat1[2].append(file_name)
		elif cat == '2':
			cat2[0].append(image_address)
			cat2[1].append(int(label))
			cat2[2].append(file_name)
		elif cat == '3':
			cat3[0].append(image_address)
			cat3[1].append(int(label))
			cat3[2].append(file_name)
		else:
			print('error')

	return cat1, cat2, cat3
	#images_addr, labels, files_name

def get_cat(image_addr, text_location_cat):
	cat = ""
	split_addr = image_addr.split("/")
	item_name = split_addr[1]
	split_item_name = item_name.split("_")
	cloth_name = split_item_name[-1]

	our_file = open(text_location_cat, 'r')
	our_file = our_file.read().splitlines()
	for our in our_file[2:]:
		our_string = "".join(our)
		our_string = our_string.split()
		if cloth_name == our_string[0]:
			return our_string[1]

	return cat

#print(get_cat('img/Sheer_Pleated-Front_Blouse/img_00000001.jpg', TEXT_LOCATION_CAT))


def label_list(text_location_label): 
	images_addr = list() #create an image addr list
	labels = list() #create a label list
	files_name = list() #create a file name list
	our_file = open(text_location_label, 'r') #open read only file
	our_file = our_file.read().splitlines() #split file into lines
	for our in itertools.islice(our_file, 2, None):  #loops through file // skips first two lines
		our_string = "".join(our) #convert the line to a string
		our_string = our_string.split() #split the line
		images_addr.append(our_string[0]) #add first item (addr) of the line to image addr list
		labels.append(int(our_string[1])) #add second item (label) of the line to label list
		file_name = '/home/kelsonl/Desktop/obj_detection/' + our_string[0] #create file name
		files_name.append(file_name) #add the name to the file name list
	return images_addr, labels, files_name #return stuff

def new_bbox_list(text_location_box, text_location_cat):
	our_file = open(text_location_box, 'r')
	our_file = our_file.read().splitlines()

	cat1 = []
	cat1.append([])
	cat1_heights = []
	cat1_widths = []
	cat1_dims = (cat1_heights, cat1_widths)
	cat1.append(cat1_dims)
	cat1_xmins = []
	cat1_xmaxs = []
	cat1_ymins = []
	cat1_ymaxs = []
	cat1_bboxs = (cat1_xmins, cat1_xmaxs, cat1_ymins, cat1_ymaxs)
	cat1.append(cat1_bboxs)

	cat2 = []
	cat2.append([])
	cat2_heights = []
	cat2_widths = []
	cat2_dims = (cat2_heights, cat2_widths)
	cat2.append(cat2_dims)
	cat2_xmins = []
	cat2_xmaxs = []
	cat2_ymins = []
	cat2_ymaxs = []
	cat2_bboxs = (cat2_xmins, cat2_xmaxs, cat2_ymins, cat2_ymaxs)
	cat2.append(cat2_bboxs)

	cat3 = []
	cat3.append([])
	cat3_heights = []
	cat3_widths = []
	cat3_dims = (cat3_heights, cat3_widths)
	cat3.append(cat3_dims)
	cat3_xmins = []
	cat3_xmaxs = []
	cat3_ymins = []
	cat3_ymaxs = []
	cat3_bboxs = (cat3_xmins, cat3_xmaxs, cat3_ymins, cat3_ymaxs)
	cat3.append(cat3_bboxs)

	for our in our_file[2:]:
		our_string = "".join(our)
		our_string = our_string.split()
		address = our_string[0]
		image = cv.imread('/home/kelsonl/Desktop/obj_detection/' + address)
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		(h, w) = image.shape[:2]
		xmin_before = float(our_string[1])
		xmax_before = float(our_string[3])
		ymin_before = float(our_string[2])
		ymax_before = float(our_string[4])
		xmin_normalized = xmin_before / w
		xmax_normalized = xmax_before / w
		ymin_normalized = ymin_before / h
		ymax_normalized = ymax_before / h

		cat = get_cat(address, text_location_cat)
		if cat == '1':
			cat1[0].append(image)
			cat1_heights.append(h)
			cat1_widths.append(w)
			cat1_xmins.append(xmin_normalized)
			cat1_xmaxs.append(xmax_normalized)
			cat1_ymins.append(ymin_normalized)
			cat1_ymaxs.append(ymax_normalized)
		elif cat == '2':
			cat2[0].append(image)
			cat2_heights.append(h)
			cat2_widths.append(w)
			cat2_xmins.append(xmin_normalized)
			cat2_xmaxs.append(xmax_normalized)
			cat2_ymins.append(ymin_normalized)
			cat2_ymaxs.append(ymax_normalized)
		elif cat == '3':
			cat3[0].append(image)
			cat3_heights.append(h)
			cat3_widths.append(w)
			cat3_xmins.append(xmin_normalized)
			cat3_xmaxs.append(xmax_normalized)
			cat3_ymins.append(ymin_normalized)
			cat3_ymaxs.append(ymax_normalized)
		else:
			print('error')

	return cat1, cat2, cat3
	#images, dims, bboxs


def bbox_list(text_location_bbox): 
	images = list() #create an image list
	heights = list() #create a height list
	widths = list() #create a width list
	dims = (heights, widths) 
	xmins = list() #create xmin list
	xmaxs = list() #create xmax list
	ymins = list() #create ymin list
	ymaxs = list() #create yamx list
	bboxs = (xmins, xmaxs, ymins, ymaxs) 
	our_file = open(text_location_bbox, 'r') #open file
	our_file = our_file.read().splitlines() #split file
	for our in itertools.islice(our_file, 2, None): #loop through file, skip first two lines
		our_string = "".join(our) #convert line to string
		our_string = our_string.split() #split line
		address = our_string[0] #get address
		image = cv.imread('/home/kelsonl/Desktop/obj_detection/' + address) #load image
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB) #change image color from BGR to RGB
		(h, w) = image.shape[:2] #get height and width
		images.append(image) #add image to list
		heights.append(h) #add height to list
		widths.append(w) #add width to list
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
	for our in itertools.islice(our_file, 2, None): #our_file[2:]
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

def new_save_to_record(images_addr, labels, files_name, images, dims, bboxs, cats, name): 
	filename = name
	writer = tf.python_io.TFRecordWriter(filename)
	if len(images_addr) != len(images): 
		raise Exception("Error: the lengths are different.") 
	length = len(images_addr) #number of images
	for i in range(length): #loop through lists
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

def save_to_record(images_addr, labels, files_name, images, dims, bboxs, cats): 
	filename = TFRECORD_NAME 
	writer = tf.python_io.TFRecordWriter(filename)
	if len(images_addr) != len(images): 
		raise Exception("Error: the lengths are different.") 
	length = len(images_addr) #number of images
	for i in range(length): #loop through lists
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

def new_run():
	cat1_label, cat2_label, cat3_label = new_label_list(TEXT_LOCATION_LABEL, TEXT_LOCATION_CAT)
	cat1_bbox, cat2_bbox, cat3_bbox = new_bbox_list(TEXT_LOCATION_BBOX, TEXT_LOCATION_CAT)
	cats = cat_list(TEXT_LOCATION_CAT)
	new_save_to_record(cat1_label[0], cat1_label[1], cat1_label[2], cat1_bbox[0], cat1_bbox[1], cat1_bbox[2], cats, 'cat1')
	new_save_to_record(cat2_label[0], cat2_label[1], cat2_label[2], cat2_bbox[0], cat2_bbox[1], cat2_bbox[2], cats, 'cat2')
	new_save_to_record(cat3_label[0], cat3_label[1], cat3_label[2], cat3_bbox[0], cat3_bbox[1], cat3_bbox[2], cats, 'cat3')
	print "Test Successful"
	return

def run():
	images_addr, labels, files_name = label_list(TEXT_LOCATION_LABEL)
	images, dims, bboxs = bbox_list(TEXT_LOCATION_BBOX)
	cats = cat_list(TEXT_LOCATION_CAT)
	example = save_to_record(images_addr, labels, files_name, images, dims, bboxs, cats)
	print "Test Successful"
	return

new_run()