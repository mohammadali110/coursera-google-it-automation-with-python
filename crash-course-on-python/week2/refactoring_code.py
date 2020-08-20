# Refactor this code to make it more readable

def f1(x, y):
	z = x*y  # the area is base*height
	print("The area is " + str(z))


# Solution
def rectangle_area(base, height):
    area = base * height # the are is base * height
    print("The area is "+str(area))

f1(5,6) # calling old function
rectangle_area(5,6) #calling refactored function