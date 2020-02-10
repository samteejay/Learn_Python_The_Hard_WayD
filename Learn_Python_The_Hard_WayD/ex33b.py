#Study Drills
#Convert this while-loop to a function that you can call, 
#and replace 6 in the test (i < 6) with a variable.
#Add another variable to the function arguments that you can pass in that lets you change
#the + 1 on line 8, so you can change how much it increments by.

numbers = []

def sample(num, inc):
	print "Here is it: "
	i = 0

	while i < num:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

print "We want to run a while-loop"

print "Enter the number"
num = int(raw_input("> "))

print "Enter the increment"
inc = int(raw_input("> "))

sample(num, inc)

for nub in numbers:
	print nub
	
	
