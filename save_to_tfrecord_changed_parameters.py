import os
import itertools 
import cv2 as cv
import numpy as np  
import tensorflow as tf
import matplotlib.pyplot as plt 
#FILL THIS OUT#
PATH_TO_FILES = '/home/young-joo/Desktop/obj_detection/' 
TEXT_LOCATION_LABEL = PATH_TO_FILES + 'short_cat.txt' 
TEXT_LOCATION_BBOX = PATH_TO_FILES + 'short_bbox.txt'
TEXT_LOCATION_CAT = PATH_TO_FILES + 'list_category_cloth.txt'
TEXT_LOCATION_PART = PATH_TO_FILES + 'short_partition.txt'
TFRECORD_NAME = 'tfrecord_is_great'

#save my address as a parameter to avoid having to retype it all the time 


def label_list_partitioned(text_location_label, text_location_part): 
        our_file = open(text_location_label, 'r')
	our_file = our_file.read().splitlines()
        #read the partition file
        partition_file = open(text_location_part, 'r')
        partition_file = partition_file.read().splitlines()
        #[0]: addr [1]: labels [2]: files_name
        training = []
        training.append([])
        training.append([])
        training.append([])
        testing = []
        testing.append([])
        testing.append([])
        testing.append([])
        validating = []
        validating.append([])
        validating.append([])
        validating.append([])
	
        for counter in range(2, len(our_file), 1):  
		our_string = "".join(our_file[counter])
                partition_string = "".join(partition_file[counter])
		our_string = our_string.split()
                partition_string = partition_string.split()
                assert partition_string[0] == our_string[0] 

		file_name = PATH_TO_FILES + our_string[0]
                if   partition_string[1] == "train":
                    training[0].append(our_string[0])
                    training[1].append(int(our_string[1]))
    		    training[2].append(file_name)
                elif partition_string[1] == "val":
                    validating[0].append(our_string[0])
                    validating[1].append(int(our_string[1]))
    		    validating[2].append(file_name)
                elif partition_string[1] == "test":
                    testing[0].append(our_string[0])  
                    testing[1].append(int(our_string[1]))
    		    testing[2].append(file_name)
                else:
                    assert (0)

	return training, testing, validating
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
		file_name = PATH_TO_FILES + our_string[0]
		files_name.append(file_name)
	return images_addr, labels, files_name 

def bbox_list_partitioned(text_location_bbox, text_location_part): 
        our_file = open(text_location_bbox, 'r')
	our_file = our_file.read().splitlines()
        #read the partition file
        partition_file = open(text_location_part, 'r')
        partition_file = partition_file.read().splitlines()
        #[0]: images [1]: dims [2]: bboxs
        training = []
        training.append([])
        training_heights = []
        training_widths = []
        training_dims = (training_heights, training_widths)
        training.append(training_dims)
        training_xmins = []
        training_xmaxs = []
        training_ymins = []
        training_ymaxs = []
        training_bboxs = (training_xmins, training_xmaxs, training_ymins, training_ymaxs)
        training.append(training_bboxs)
        
        testing = []
        testing.append([])
        testing_heights = []
        testing_widths = []
        testing_dims = (testing_heights, testing_widths)
        testing.append(testing_dims)
        testing_xmins = []
        testing_xmaxs = []
        testing_ymins = []
        testing_ymaxs = []
        testing_bboxs = (testing_xmins, testing_xmaxs, testing_ymins, testing_ymaxs)
        testing.append(testing_bboxs)
        
        validating = []
        validating.append([])
        validating_heights = []
        validating_widths = []
        validating_dims = (validating_heights, validating_widths)
        validating.append(validating_dims)
        validating_xmins = []
        validating_xmaxs = []
        validating_ymins = []
        validating_ymaxs = []
        validating_bboxs = (validating_xmins, validating_xmaxs, validating_ymins, validating_ymaxs)
        validating.append(validating_bboxs)

        for counter in range(2, len(our_file), 1):
		our_string = "".join(our_file[counter])
                partition_string = "".join(partition_file[counter])
		our_string = our_string.split() 
                partition_string = partition_string.split()
                assert partition_string[0] == our_string[0]
		address = our_string[0]
		
                image = cv.imread(PATH_TO_FILES + address)
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
                
                if partition_string[1] == "train":
                    training[0].append(image)
                    training_heights.append(h)
                    training_widths.append(w)
                    training_xmins.append(xmin_normalized)
                    training_xmaxs.append(xmax_normalized)
                    training_ymins.append(ymin_normalized)
                    training_ymaxs.append(ymax_normalized) 
                elif partition_string[1] == "val":
                    validating[0].append(image)
                    validating_heights.append(h)
                    validating_widths.append(w)
                    validating_xmins.append(xmin_normalized)
                    validating_xmaxs.append(xmax_normalized)
                    validating_ymins.append(ymin_normalized)
                    validating_ymaxs.append(ymax_normalized) 
                elif partition_string[1] == "test":
                    testing[0].append(image)
                    testing_heights.append(h)
                    testing_widths.append(w)
                    testing_xmins.append(xmin_normalized)
                    testing_xmaxs.append(xmax_normalized)
                    testing_ymins.append(ymin_normalized)
                    testing_ymaxs.append(ymax_normalized) 
                else:
                    assert(0)
                
	return training, testing, validating 
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
		image = cv.imread(PATH_TO_FILES + address)
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		(h, w) = image.shape[:2]
		images.append(image)
		heights.append(h)
		widths.append(w)
		xmin_before = float(our_string[1])
		xmax_before = float(our_string[3])
		ymin_before = float(our_string[2])
		ymax_before = float(our_string[4])
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

def save_to_record(images_addr, labels, files_name, images, dims, bboxs, cats, option = None): 
        if option == None: 
            filename = TFRECORD_NAME 
        else: 
            filename = option
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
if __name__ == '__main__':
#   images_addr, labels, files_name = label_list(TEXT_LOCATION_LABEL)
    training_label, testing_label, validating_label = label_list_partitioned(TEXT_LOCATION_LABEL, TEXT_LOCATION_PART)
#   images, dims, bboxs = bbox_list(TEXT_LOCATION_BBOX)
    training_bbox, testing_bbox, validating_bbox = bbox_list_partitioned(TEXT_LOCATION_BBOX, TEXT_LOCATION_PART)
    cats = cat_list(TEXT_LOCATION_CAT)
#   example = save_to_record(images_addr, labels, files_name, images, dims, bboxs, cats)

    ########GENERATE TRAINING DATA########
    assert len(training_label[0]) == len(training_bbox[0])
    assert len(training_label[1]) == len(training_bbox[1][1])
    assert len(training_label[2]) == len(training_bbox[2][1])
    example = save_to_record(training_label[0],#images_addr 
                             training_label[1],#labels 
                             training_label[2],#files_name 
                             training_bbox[0],#images
                             training_bbox[1],#dims
                             training_bbox[2],#bboxs
                             cats, 
                             'training') #option

    ########GENERATE TESTING DATA########
    assert len(testing_label[0]) == len(testing_bbox[0])
    assert len(testing_label[1]) == len(testing_bbox[1][1])
    assert len(testing_label[2]) == len(testing_bbox[2][1])
    example = save_to_record(testing_label[0],#images_addr 
                             testing_label[1],#labels 
                             testing_label[2],#files_name 
                             testing_bbox[0],#images
                             testing_bbox[1],#dims
                             testing_bbox[2],#bboxs
                             cats, 
                             'testing') #option

    ########GENERATE VALIDATION DATA########
    assert len(validating_label[0]) == len(validating_bbox[0])
    assert len(validating_label[1]) == len(validating_bbox[1][1])
    assert len(validating_label[2]) == len(validating_bbox[2][1])
    example = save_to_record(validating_label[0],#images_addr 
                             validating_label[1],#labels 
                             validating_label[2],#files_name 
                             validating_bbox[0],#images
                             validating_bbox[1],#dims
                             validating_bbox[2],#bboxs
                             cats, 
                             'validation') #option
    print "Test Successful"
