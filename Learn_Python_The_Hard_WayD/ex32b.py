#Study Drills

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
two = [[1, 2, 3], [7, 8, 9]]

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
for i in change:
	print "I got %r" % i
	
elements = []

for i in range(0, 6):
	print "Adding this %d to the list" %i
	elements.append(i)
	
for i in elements:
	print "Elements was: %d" %i
	
for i in two:
	print "This is a 2D list: %r" %i


