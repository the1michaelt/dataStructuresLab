# months=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")


# def month_of_Pi(months):
#     """
#     Task 1a: Tuple is the best data strategy for months of the year which will never change.
#     """
#     count= 0
#     stop= len(months)-1
#     while count <= stop:
#         Pi= 3.14
#         Pi= int(Pi)
#         if count == (Pi-1): 
#             print('\nScenario 1a: Tuple. The month of Pi is {}.'.format(months[count]))
#             break
#         else:
#             count+=1

# # # def print_month_of_pi():
# # #       months = ("January", "February", "March", "April")
# # #       pi = 3.14
# # #       correct_month_number = int(pi)
# # #       print(f"The Pi Month is {months[correct_month_number - 1]}")


# month_of_Pi(months)


# def print_favorite_fruits_veggies():
#     """
#     Task 1b: Set is the best data strategy for SEPARATE SOURCES, collated together.
#     """
#     two_favorite_fruits = {"strawberries", "raspberries"}
#     two_favorite_vegetables = {"eggplant", "carrots"}
#     five_fruits_or_vegetables = {"passionfruit"}

#     five_fruits_or_vegetables.update(two_favorite_fruits)
#     five_fruits_or_vegetables.update(two_favorite_vegetables)
#     print('\nScenario 1b: Set')
   
#     for produce in five_fruits_or_vegetables:
#         print(produce)

# print_favorite_fruits_veggies()


# # user_profile = {}. 
# # The profile should consist of the following information:
# # task 1c

# def print_profile():
#     """
#     Task 1c: Dictionary is the best data strategy to collect pieces of each user's data.
#     """
#     user_profile = {
#         "First_Name": "Joe",
#         "Last_Name": "Moe",
#         "Email_Address":"nomojoemoe@yafoo.com",
#         "Phone_Number":"03030300303",
#         "Relation to me":"brother",
#     }
#     # print(user_profile["First_Name"])
#     print('\nScenario 1c: Dictionary with literal string interpolation')
#     # items = user_profile.items()
#     # print(items)
#     # keys = user_profile.keys()
#     # print(keys)
#     values = user_profile.values()
#     print(values)
# print_profile()


# task 2: 
def print_relative_profile():
    """
    Task 2 uses nested dictionaries to collect multiple users' data.
    """
    relatives_profile = {"close_kin":[{"First_Name": "Joe", "Relation_to_me": "brother",},
        {"First_Name": "Sue", "Relation_to_me": "mother",},
        {"First_Name": "Boe", "Relation_to_me": "father", },],}
           
    
    print('\nTask 2: Iterate through the list, printing first name and relationship')
    # for key, value in relatives_profile:
    #     print(f"{key}:{value}")
    print(relatives_profile["close_kin"]["First_Name"])
   
print_relative_profile()

# TEST
def print_relative_profile():
    """_summary_
    """
    user_profile = {
        "First_Name": "Joe",
        "Last_Name": "Moe",
        "Email_Address":"nomojoemoe@yafoo.com",
        "Phone_Number":"03030300303",
        "Relation_to_me":"brother",
    }
    
#     # print(user_profile["First_Name"])
#     print('\nTask 2: Dictionary: iterate through the list, printing first name and relationship')
#     for relative in user_profile.values():
#         print(relative)


items = user_profile.items(user_profile[0], user_profile[4])
print(items)
    
print_relative_profile()

# # Task 1: Dictionary, Set and Tuple
# # # Given the following three scenarios, choose the best data structure (between a dictionary, set, or tuple) to efficiently store the data. Each scenario ties directly to one data structure. Each data structure will be used only once. You will need to determine which data structure is best for which scenario, and then implement the data structure in Python.
# # # 1. Store the months of the year as strings. Determine the month in the data structure in which National Pi Day exists and print that month to the console. 
# # # 1. HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.
# # 2. Store five fruits or vegetables.
# # 1. Add two of your favorite fruits and two of your favorite vegetables to the collection.
# # 2. Iterate over the collection and print each one to the console. 
# # 3. Store information about a user profile. Use literal string interpolation to print the user’s profile information to the console. The profile should consist of the following information:
# # 1. First Name
# # 2. Last Name
# # 3. Email Address
# # 4. Phone Number


# # Helpful Hint:
# # For more information on “string interpolation” refer to this article:
# # There are at least 6 different ways to do this.
# # https://therenegadecoder.com/code/how-to-format-a-string-in-python/

# # Task 2: List of Dictionaries
# # Use a list to store the dictionary of your immediate family members, with each index of the list storing its own dictionary. Dictionary should contain the following keys:
# # First name
# # Last name
# # Relation to you

# # Once you have stored the List of Dictionary items, write a function/method that will iterate over the List and print off the First Name and Relation of each person in the List.
