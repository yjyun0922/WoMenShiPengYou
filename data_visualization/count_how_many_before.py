import os 
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

FILE_ADDRESS = '/home/young-joo/Desktop/obj_detection/list_category_img_before.txt'

#MUST DO IT ACCORING TO THE NUMBER LABELS 
def count_num(file_address):
	our_file = open(file_address, 'r')
	our_file = our_file.read().splitlines()
	
	anorak = 0  
	blazer = 0 
	blouse = 0 
	bomber = 0 
	button_down = 0 
	cardigan = 0 
	flannel = 0 
	halter = 0 
	henley = 0 
	hoodie = 0 

	jacket = 0 
	jersey = 0 
	parka = 0 
	peacoat = 0 
	poncho = 0 
	sweater = 0 
	tank = 0 
	tee = 0 
	top = 0 
	turtleneck = 0 

	capris = 0 
	chinos = 0 
	culottes = 0 
	cutoffs = 0 
	gauchos = 0 
	jeans = 0 
	jeggings = 0 
	jodhpurs = 0 
	joggers = 0 
	leggings = 0 

	sarong = 0 
	shorts = 0 
	skirt = 0 
	sweatpants = 0 
	sweatshorts = 0 
	trunks = 0 
	caftan = 0 
	cape = 0
	coat = 0
	coverup = 0
								
	dress = 0 
	jumpsuit = 0 
	kaftan = 0 
	kimono = 0 
	nightdress = 0 
	onesie = 0 
	robe = 0 
	romper = 0 
	shirtdress = 0 
	sundress = 0 

	for counter in range(2, len(our_file), 1): 
		our_string = "".join(our_file[counter])
		our_string = our_string.split()
		label = our_string[1]
		if label == '1': 
			anorak += 1
		elif label == '2': 
			blazer += 1
		elif label == '3': 
			blouse += 1
		elif label == '4': 
			bomber += 1
		elif label == '5': 
			button_down += 1
		elif label == '6': 
			cardigan += 1
		elif label == '7': 
			flannel += 1
		elif label == '8': 
			halter += 1
		elif label == '9': 
			henley += 1
		elif label == '10': 
			hoodie += 1

		elif label == '11': 
			jacket += 1
		elif label == '12': 
			jersey += 1
		elif label == '13': 
			parka += 1
		elif label == '14': 
			peacoat += 1
		elif label == '15': 
			poncho += 1
		elif label == '16': 
			sweater += 1
		elif label == '17': 
			tank += 1
		elif label == '18': 
			tee += 1
		elif label == '19': 
			top += 1
		elif label == '20': 
			turtleneck += 1

		elif label == '21': 
			capris += 1
		elif label == '22': 
			chinos += 1
		elif label == '23': 
			culottes += 1
		elif label == '24': 
			cutoffs += 1
		elif label == '25': 
			gauchos += 1
		elif label == '26': 
			jeans += 1
		elif label == '27': 
			jeggings += 1
		elif label == '28': 
			jodhpurs += 1
		elif label == '29': 
			joggers += 1
		elif label == '30': 
			leggings += 1

		elif label == '31': 
			sarong += 1
		elif label == '32': 
			shorts += 1
		elif label == '33': 
			skirt += 1
		elif label == '34': 
			sweatpants += 1
		elif label == '35': 
			sweatshorts += 1
		elif label == '36': 
			trunks += 1
		elif label == '37': 
			caftan += 1
		elif label == '38': 
			cape += 1
		elif label == '39': 
			coat += 1
		elif label == '40': 
			coverup += 1

		elif label == '41': 
			dress += 1
		elif label == '42': 
			jumpsuit += 1
		elif label == '43': 
			kaftan += 1
		elif label == '44': 
			kimono += 1
		elif label == '45': 
			nightdress += 1
		elif label == '46': 
			onesie += 1
		elif label == '47': 
			robe += 1
		elif label == '48': 
			romper += 1
		elif label == '49': 
			shirtdress += 1
		elif label == '50': 
			sundress += 1
       
	categories = range(1, 51)	
	y_pos = np.arange(len(categories))
	num_of_items = [anorak, blazer, blouse, bomber, button_down, 
		        cardigan, flannel, halter, henley, hoodie, 
			jacket, jersey, parka, peacoat, poncho, 
			sweater, tank, tee, top, turtleneck, 
			capris, chinos, culottes, cutoffs, gauchos, 
			jeans, jeggings, jodhpurs, joggers, leggings, 
			sarong, shorts, skirt, sweatpants, sweatshorts, 
			trunks, caftan, cape, coat, coverup, 
			dress, jumpsuit, kaftan, kimono, nightdress, 
			onesie, robe, romper, shirtdress, sundress] 
	plt.bar(y_pos, num_of_items, align='center', alpha=0.5)
	plt.xticks(y_pos, categories)
	plt.xlabel('Categories')
	plt.ylabel('Num of Items')
	plt.title('Num of Items in Each Category')
	
	plt.show()

count_num(FILE_ADDRESS)



