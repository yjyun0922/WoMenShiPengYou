BEFORE_FILE = '/home/young-joo/Desktop/Programs_for_Cleaning_Data/list_category_cloth_before.txt'
AFTER_FILE = '/home/young-joo/Desktop/Programs_for_Cleaning_Data/list_category_cloth_after.txt' 

before = {}
after = {}
def enter_dict(before_file, after_file): 
	our_before = open(before_file, 'r')
	our_before = our_before.read().splitlines() 
	for counter in range(2, len(our_before), 1): 
		our_string = "".join(our_before[counter])
		our_string = our_string.split() 
		before[our_string[1]] = our_string[0]
	our_after = open(after_file, 'r')
	our_after = our_after.read().splitlines()
	for counter in range(2, len(our_after), 1): 
		our_string = "".join(our_after[counter])
		our_string = our_string.split()
		after[our_string[1]] = our_string[0]
enter_dict(BEFORE_FILE, AFTER_FILE) 



