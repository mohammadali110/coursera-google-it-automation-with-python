# def retry(operation, attempts):
#   for n in range(attempts):
#     if operation():
#         print("Attempt " + str(n) + " succeeded")
#         break
#     else:
#         print("Attempt " + str(n) + " failed")
# retry(create_user, 3)
# retry(stop_service, 5)


# number = 0

# for number in range(10):
#     if number == 5:
#         break    # break here

#     print('Number is ' + str(number))

# print('Out of loop')

def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
        print("x ="+str(x))
    return result

for n in range(1,11):
    print(n, factorial(n+1))