# iteration pattern
# doing the same thing once for each member of a list

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	for i in range(0, len(list)):
		list[i] += 1

	return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"

#accumulation pattern - type of iteration
#keep track of other data as we go

def sum(list):
	total = 0
	for n in list:
		total += n

	return total

def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

# HW 
	#a funtion - average
	#b 2nd function also finds average but drops lowest 2 scores

def average(list):
	total = 0
	for n in list:
		total += n
	average = total / len(list)

	return average

def drop_2(list):
	for counter in range (2):
		current_min = list[0]
		for n in list:
			if n < current_min:
				current_min = n

		list.remove(current_min)

def average_drop2(list):
	drop_2(list)

	total = 0
	for n in list:
		total += n
	average = total / float(len(list))

	return average