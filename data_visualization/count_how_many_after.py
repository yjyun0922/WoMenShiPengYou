import os 
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

FILE_ADDRESS = '/home/young-joo/Desktop/obj_detection/list_category_img_after.txt'

#MUST DO IT ACCORING TO THE NUMBER LABELS 
def count_num(file_address):
	our_file = open(file_address, 'r')
	our_file = our_file.read().splitlines()

	cardiagn = 0 
	blazer = 0 
	outerwear = 0 
	hoodie = 0 
	sweater = 0 
	miscellaneous_long_sleeve_top = 0
 
	short_sleeve_top = 0 
	sleeveless_top = 0
	long_full_body_wear = 0 
	short_full_body_wear = 0 
	baggy_pants = 0 
	jeans = 0 
		
	long_exercise_pants = 0 
	miscellaneous_long_pants = 0 
	hotpants = 0 
	miscellaneous_shorts = 0 
	miniskirt = 0 
	miscellaneous_skirt = 0  

	for counter in range(2, len(our_file), 1): 
		our_string = "".join(our_file[counter])
		our_string = our_string.split()
		label = our_string[1]
		if label == '1': 
			cardigan += 1
		elif label == '2': 
			blazer += 1
		elif label == '3': 
			outerwear += 1
		elif label == '4': 
			hoodie += 1
		elif label == '5': 
			sweater += 1
		elif label == '6': 
			miscellaneous_long_sleeve_top += 1

		elif label == '7': 
			short_sleeve_top += 1
		elif label == '8': 
			sleeveless_top += 1
		elif label == '9': 
			long_full_body_wear += 1
		elif label == '10': 
			short_full_body_wear += 1
		elif label == '11': 
			baggy_pants += 1
		elif label == '12': 
			jeans += 1

		elif label == '13': 
			long_exercise_pants += 1
		elif label == '14': 
			miscellaneous_long_pants += 1
		elif label == '15': 
			hotpants += 1
		elif label == '16': 
			miscellaneous_shorts += 1
		elif label == '17': 
			miniskirt += 1
		elif label == '18': 
			miscellaneous_skirt += 1

		categories = range(1, 19)	
	y_pos = np.arange(len(categories))
	num_of_items = [cardigan, blazer, outerwear, 
			hoodie, sweater, miscellaneous_long_sleeve_top, 
			short_sleeve_top, sleeveles_top, long_full_body_wear, 
			short_full_body_wear, baggy_pants, jeans, 
			long_exercise_pants, miscellaneous_long_pants, hotpants, 
			miscellaneous_shorts, miniskirt, miscellaneous_skirt] 
	plt.bar(y_pos, num_of_items, align='center', alpha=0.5)
	plt.xticks(y_pos, categories)
	plt.xlabel('Categories')
	plt.ylabel('Num of Items')
	plt.title('Num of Items in Each Category')
	
	plt.show()



