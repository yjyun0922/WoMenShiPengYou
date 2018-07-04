import os
import itertools 

TEXT_LOCATION_CAT = '/home/yjyun0922/Desktop/WoMenShiPengYou/TFRecord/Files/list_category_cloth.txt'

label_dict = {} 

def cat_list(text_location_cat): 
	cats = list()
	our_file = open(text_location_cat, 'r')
	our_file = our_file.read().splitlines()
	for our in itertools.islice(our_file, 2, None): 
		our_string = "".join(our)
		our_string = our_string.split()
		cats.append(our_string[0])
	return cats

cats = cat_list(TEXT_LOCATION_CAT)

for i in range(1, 51, 1): 
	label_dict['{}'.format(i)] = cats[i-1]

