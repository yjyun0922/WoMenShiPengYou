import numpy as np 
import xml.etree.ElementTree as ET

#Should be the same directory as the img folder
PATH_TO_TEXT_FILE = '/home/young-joo/Desktop/Working_Directory/'

#initializing the tree 
tree = ET.parse('1.xml')
root = tree.getroot()

my_array = []
for i in range(1, 201):
	my_array.append([]) 
	#initializing the tree 
	tree = ET.parse('%d.xml' % i)
	root = tree.getroot()
	num = i - 1  
	for coord in root.iter('bndbox'):
		counter_2 = 0 
		for elem in coord.iter():
			if counter_2 != 0: 
				my_array[num].append(elem.text)
			counter_2 += 1

#write everything into a text file
print my_array

#generating the bbox file 
donefile = open(PATH_TO_TEXT_FILE + "bbox_sweater.txt", "w")
i = 0 
for i in range(200): 
	xmin = my_array[i][0]
	ymin = my_array[i][1]
	xmax = my_array[i][2]
	ymax = my_array[i][3]
	donefile.write(("img/Cute_7_Sweater/%d.jpg" % (i + 1)) + " " + xmin + " " + ymin + " " + xmax + " " + ymax + "\n") 
donefile.close()

#generating the label file 
donefile = open(PATH_TO_TEXT_FILE + "label_sweater.txt", "w") 
for i in range(1, 201): 
	donefile.write(("img/Cute_7_Sweater/%d.jpg" % i) + " " + "11\n") 
donefile.close() 












