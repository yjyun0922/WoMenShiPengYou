import random

def get_1000():
	our_file = open('cat_donefile.txt','r')
	our_file = our_file.readlines()
	our_list = []
	count = 1
	for i in range(len(our_file)):
		our_list.append(our_file[i])
		count = count + 1
		if count > 1000:
			break
	return our_list

def distribute(the_list):
	our_list = the_list
	new_list = []
	count = 0
	for i in range(len(our_list)):
		string = our_list[i].strip()
		count = count + 1
		if count < 801:
			string = string + "\ttrain\n"
		else:
			string = string + "\ttest\n"
		new_list.append(string)
	return new_list

def get_num(line):
	new_line = line
	new_line = new_line.strip()
	new_line = new_line.split()
	new_line = new_line[0]
	new_line = new_line.split("/")
	new_line = new_line[1]
	new_line = new_line.split(".")
	new_line = new_line[0]
	return int(new_line)

our_list = get_1000()
random.shuffle(our_list)
our_list = distribute(our_list)
our_list.sort(key=get_num)

new_file = open('new_file.txt','w')
for line in our_list:
	new_file.write(line)
