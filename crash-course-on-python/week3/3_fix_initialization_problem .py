# In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?
current=0
def count_down(start_number):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

# Solution: 
# current should be initialized by the given parameter of start_number
# Also it should be defined within the function

def count_down(start_number):
  current=start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)