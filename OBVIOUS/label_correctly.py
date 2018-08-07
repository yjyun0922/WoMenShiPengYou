import os

PATH_TO_FILES = '/home/young-joo/Desktop/Cleaning_Complete/label/'
ADDR = PATH_TO_FILES + 'label_thick_cotton_sweater.txt'
LABEL_NUM = '1'

our_file = open(ADDR, 'r')
our_file = our_file.read().splitlines()
donefile = open(PATH_TO_FILES + 'correct', 'w')
for our in our_file: 
	our_string = "".join(our)
	our_string = our_string.split()
	donefile.write(our_string[0] + " " + LABEL_NUM + "\n")
donefile.close()
