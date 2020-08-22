# The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?

# def print_range(start, end):
# 	# Loop through the numbers from start to end
# 	n = start
# 	while n <= end:
# 		print(n)

# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# Solution
# Variable n's value is not being incremented. We need to increment the value.
# Here is the example


def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
    
	while n <= end:
		print(n)
        n+=1                                                                                                                                                                                                                                                                                                                                            

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 