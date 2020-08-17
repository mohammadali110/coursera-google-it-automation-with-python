
# Example: keyword = none
def a_void_function():
    a = 1
    b = 2
    c = a + b

x = a_void_function() # Function does not return anything
print(x) # should print none


def improper_return_function(a):
    if (a % 2) == 0:
        return True

x = improper_return_function(4) # For all odd numbers, function returns nothing, so it should print none.
print(x) # none for odd numbers, True for even numbers