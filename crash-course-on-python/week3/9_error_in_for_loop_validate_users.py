# The validate_users function is used by the system to check if a list of users is valid or invalid. 
# A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. 
# When calling it like in this example, something is not right. Can you figure out what to fix?

# def validate_users(users):
#   for user in users:
#     if is_valid(user):
#       print(user + " is valid")
#     else:
#       print(user + " is invalid")

# validate_users("purplecat")

# Solution: pass the arument in validate_users as a list e.g. validate_user(["purplecate"])

def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

# Creating our own is_valid function
def is_valid(username):
    if len(username) >= 2:
        return True
    else:
        return False


validate_users(["purplecat"])