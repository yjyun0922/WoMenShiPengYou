import os
import itertools 
import cv2 as cv
import numpy as np  
import tensorflow as tf
import matplotlib.pyplot as plt

#PLEASE HAVE ALL THE FILES YOU NEED TOGETHER IN ONE FILE# 
#FILL IN THE PATH TO THE FOLDER THAT CONTAINS ALL OF YOUR FILES#
PATH_TO_FILES = '/home/young-joo/Desktop/obj_detection/'
 
#YOU DON'T NEED TO CHANGE ANY OF THIS 
TEXT_LOCATION_LABEL = PATH_TO_FILES + 'list_category_img.txt' 
TEXT_LOCATION_BBOX = PATH_TO_FILES + 'list_bbox.txt'
TEXT_LOCATION_CAT = PATH_TO_FILES + 'list_category_cloth.txt'
TEXT_LOCATION_PART = PATH_TO_FILES + 'list_eval_partition.txt'

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
        training_xmins = []
        training_xmaxs = []
        training_ymins = []
        training_ymaxs = []
        training_bboxs = (training_xmins, training_xmaxs, training_ymins, training_ymaxs)
        training.append(training_bboxs)
        
        testing = []
        testing_xmins = []
        testing_xmaxs = []
        testing_ymins = []
        testing_ymaxs = []
        testing_bboxs = (testing_xmins, testing_xmaxs, testing_ymins, testing_ymaxs)
        testing.append(testing_bboxs)
        
        validating = []
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
		xmin = float(our_string[1])
		xmax = float(our_string[3])
		ymin = float(our_string[2])
		ymax = float(our_string[4])
                
                if partition_string[1] == "train":
                    training_xmins.append(xmin)
                    training_xmaxs.append(xmax)
                    training_ymins.append(ymin)
                    training_ymaxs.append(ymax) 
                elif partition_string[1] == "val": 
                    validating_xmins.append(xmin)
                    validating_xmaxs.append(xmax)
                    validating_ymins.append(ymin)
                    validating_ymaxs.append(ymax) 
                elif partition_string[1] == "test": 
                    testing_xmins.append(xmin)
                    testing_xmaxs.append(xmax)
                    testing_ymins.append(ymin)
                    testing_ymaxs.append(ymax) 
                else:
                    assert(0)
                
	return training, testing, validating 

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

def save_to_record(images_addr, labels, files_name, bboxs, cats, option = None): 
        if option == None: 
            filename = TFRECORD_NAME 
        else: 
            filename = option
	writer = tf.python_io.TFRecordWriter(filename)
	length = len(images_addr)
	count = 0
	for i in range(length):
		if count % 1000 == 0: 
			print("%d out of %d saved" % (count, length)) 
		image = cv.imread(PATH_TO_FILES + images_addr[i])
		image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
		(h, w) = image.shape[:2]
                ######Adding this two lines to try
		split = images_addr[i].split(".")
		with tf.gfile.GFile(PATH_TO_FILES + split[0] + "revised.jpg", 'rb') as fid:
			encoded_jpg = fid.read()
		label_num = labels[i]
		example = tf.train.Example(features=tf.train.Features(feature={
			'image/height': int64_feature(299),
  			'image/width': int64_feature(299),
  			'image/filename': bytes_feature(files_name[i].encode()),
  			'image/source_id': bytes_feature(files_name[i].encode()),
  			'image/encoded': bytes_feature(encoded_jpg),
  			'image/format': bytes_feature(b'jpg'),
      		'image/object/bbox/xmin': float_list_feature([bboxs[0][i] / w]),
      		'image/object/bbox/xmax': float_list_feature([bboxs[1][i] / w]),
      		'image/object/bbox/ymin': float_list_feature([bboxs[2][i] / h]),
      		'image/object/bbox/ymax': float_list_feature([bboxs[3][i] / h]),
      		'image/object/class/text': bytes_feature(cats[label_num-1].encode()),
      		'image/object/class/label': int64_feature(labels[i])
		}))
		writer.write(example.SerializeToString())
		count = count + 1
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
 
    example = save_to_record(training_label[0],#images_addr 
                             training_label[1],#labels 
                             training_label[2],#files_name 
                             training_bbox[0], #bbox
                             cats, 
                             'training_jpg') #option

    ########GENERATE TESTING DATA########
    example = save_to_record(testing_label[0],#images_addr 
                             testing_label[1],#labels 
                             testing_label[2],#files_name 
                             testing_bbox[0],#bboxs
                             cats, 
                             'testing_jpg') #option

    ########GENERATE VALIDATION DATA########
    example = save_to_record(validating_label[0],#images_addr 
                             validating_label[1],#labels 
                             validating_label[2],#files_name 
                             validating_bbox[0], #bboxs
                             cats, 
                             'validation_jpg') #option
    print "Test Successful"
