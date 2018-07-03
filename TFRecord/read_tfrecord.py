import os
import itertools 
import cv2 as cv
import numpy as np 
from PIL import Image 
import matplotlib.pyplot as plt 
import tensorflow as tf

#FILL THIS OUT# 
record = 'tfrecord_is_great'
BATCH_SIZE = 15
NUM_BATCH = 3

def read_and_decode(tfrecords_file, batch_size):
    filename_queue = tf.train.string_input_producer([tfrecords_file], shuffle=True)
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(
        serialized_example,
        features = {
            'image/height': tf.FixedLenFeature([], tf.int64),
            'image/width': tf.FixedLenFeature([], tf.int64),
            'image/filename': tf.FixedLenFeature([], tf.string),
            'image/source_id': tf.FixedLenFeature([], tf.string),
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
    image = tf.decode_raw(features['image/encoded'], tf.uint8)
    image = tf.reshape(image, tf.stack([height, width, 3]))
    resized_image = tf.image.resize_image_with_crop_or_pad(image=image, 
                                            target_height=300,
                                            target_width=300)
    images, labels = tf.train.shuffle_batch([resized_image, label], 
                                                batch_size = BATCH_SIZE,
                                                num_threads = 1, 
                                                capacity=100, 
                                                min_after_dequeue=10)
    return images, labels  

images, labels = read_and_decode(record, batch_size=BATCH_SIZE)

def plot_images(images, labels): 
    for i in np.arange(0, BATCH_SIZE): 
        plt.subplot(10, 10, i+1)
        plt.axis('off')
        plt.imshow(images[i])
        plt.title(labels[i])
    plt.show()

with tf.Session() as sess: 
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    for i in range(NUM_BATCH): 
        image_plot, label_plot = sess.run([images, labels])
        plot_images(image_plot, label_plot)
    print "Decoded Successfully"
    coord.request_stop()
    coord.join(threads)