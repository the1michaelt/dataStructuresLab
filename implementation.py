def month_of_Pi(months):
    """
    Task 1a: Tuple is the best data strategy for months of the year which will never change.

    Big O notation is linear, O(n).
    """
   
    count=0
    stop=len(months)-1
    while count <= stop:
        Pi=3.14
        Pi=int(Pi)
        if count == (Pi-1):
            print('Scenario 1: The month of Pi is {}.'.format(months[count]))
            break
        else:
            count += 1




# class Task3


# Task 1: Dictionary, Set and Tuple
# # Given the following three scenarios, choose the best data structure (between a dictionary, set, or tuple) 
# # to efficiently store the data. Each scenario ties directly to one data structure. 
# # Each data structure will be used only once. 



# the month in the data structure in which National Pi Day exists == March (int)
# print that month to the console. 

# # 1. HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.
# # 2. Store 


def print_favorite_fruits_veggies():
    five_fruits_or_vegetables=["strawberries", "raspberries", "blueberries", "kiwifruit", "passionfruit"]

# print_favorite_fruits_veggies()

# b) set of changeable items that are grouped
# Add two_favorite_fruits and two_favorite_vegetables
# # Iterate over the collection and print each one to the console. 
# for __ in ___ : 
#     print()

# c) dictionary-- user info contained together
# user_profile = {}. Use literal string interpolation to print the user’s profile information to the console. 
# The profile should consist of the following information:
# First_Name
# Last_Name
# Email_Address
# Phone_Number


# # Helpful Hint:
# # For more information on “string interpolation” refer to this article:
# # There are at least 6 different ways to do this.
# https://therenegadecoder.com/code/how-to-format-a-string-in-python/

# # Task 2: List of Dictionaries
# # Use a list to store the dictionary of your immediate family members, with each index of the list storing its own dictionary. Dictionary should contain the following keys:
# family_members = {}
# First_name
# Last_name
# Relation_to_you

# # Once you have stored the List of Dictionary items, write a function/method that will iterate over the List and print off the First Name and Relation of each person in the List.
