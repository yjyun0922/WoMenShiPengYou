import os
import itertools 
import cv2 as cv
import numpy as np 
from PIL import Image 
import matplotlib.pyplot as plt 
import tensorflow as tf

#FILL THIS OUT# 
file_names = ['train', 'test']
BATCH_SIZE = 5
NUM_BATCH = 3

def read_and_decode(tfrecords_file, batch_size):
    filename_queue = tf.train.string_input_producer([tfrecords_file], shuffle=True, num_epochs=5)
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(
        serialized_example,
        features = {
            'image/height': tf.FixedLenFeature([], tf.int64),
            'image/width': tf.FixedLenFeature([], tf.int64),
            'image/encoded': tf.FixedLenFeature([], tf.string),
            'image/format': tf.FixedLenFeature([], tf.string),
            'image/object/bbox/xmin': tf.VarLenFeature(tf.float32),
            'image/object/bbox/xmax': tf.VarLenFeature(tf.float32),
            'image/object/bbox/ymin': tf.VarLenFeature(tf.float32),
            'image/object/bbox/ymax': tf.VarLenFeature(tf.float32),
            'image/object/class/text': tf.FixedLenFeature([], tf.string),
            'image/object/class/label': tf.FixedLenFeature([], tf.int64)
        })
    label = tf.cast(features['image/object/class/label'], tf.int32)
    text = tf.cast(features['image/object/class/text'], tf.string)
    height = tf.cast(features['image/height'], tf.int32)
    width = tf.cast(features['image/width'], tf.int32)
    image = tf.image.decode_jpeg(features['image/encoded'])
    image = tf.reshape(image, tf.stack([height, width, 3]))
    resized_image = tf.image.resize_image_with_crop_or_pad(image=image, 
                                            target_height=299,
                                            target_width=299)
    images, labels = tf.train.shuffle_batch([resized_image, label], 
                                                batch_size = BATCH_SIZE,
                                                num_threads = 1, 
                                                capacity=100, 
                                                min_after_dequeue=10,
						allow_smaller_final_batch=True)
    return images, labels  

def plot_images(images, labels): 
    if len(images) < BATCH_SIZE:
        for i in np.arange(0, len(images)): 
            plt.subplot(10, 10, i+1)
            plt.axis('off')
            plt.imshow(images[i])
            plt.title(labels[i])
    else:
        for i in np.arange(0, BATCH_SIZE): 
            plt.subplot(10, 10, i+1)
            plt.axis('off')
            plt.imshow(images[i])
            plt.title(labels[i])
    plt.show()

def run(filename, batchsize, numbatch):
    images, labels = read_and_decode(filename, batch_size=batchsize)

    with tf.Session() as sess: 
        sess.run(tf.local_variables_initializer())
        sess.run(tf.global_variables_initializer()) 
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        for i in range(numbatch): 
            image_plot, label_plot = sess.run([images, labels])
            plot_images(image_plot, label_plot)
        print "Decoded Successfully"
        coord.request_stop()
	coord.join(threads)

#opens the images
run('train', BATCH_SIZE, NUM_BATCH)
run('test', BATCH_SIZE, NUM_BATCH)
