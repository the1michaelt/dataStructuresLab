
def month_of_Pi():
    """
    Task 1a: Tuple is the best data strategy for months of the year which will never change.
    """
    months=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    count= 0
    stop= len(months)-1
    while count <= stop:
        Pi= 3.14
        Pi= int(Pi)
        if count == (Pi-1):
            print('\nScenario 1a: Tuple. The month of Pi is {}.'.format(months[count]))
            break
        else:
            count+=1

# # def print_month_of_pi():
# #       months = ("January", "February", "March", "April")
# #       pi = 3.14
# #       correct_month_number = int(pi)
# #       print(f"The Pi Month is {months[correct_month_number - 1]}")


def print_favorite_fruits_veggies():
    """
    Task 1b: Set is the best data strategy for SEPARATE SOURCES, collated together.
    """
    two_favorite_fruits = {"strawberries", "raspberries"}
    two_favorite_vegetables = {"eggplant", "carrots"}
    five_fruits_or_vegetables = {"passionfruit"}

    five_fruits_or_vegetables.update(two_favorite_fruits)
    five_fruits_or_vegetables.update(two_favorite_vegetables)
    print('\nScenario 1b: Set')

    for produce in five_fruits_or_vegetables:
        print(produce)

# user_profile = {}.
# The profile should consist of the following information:
# task 1c

def print_profile():
    """
    Task 1c: Dictionary is the best data strategy to collect pieces of each user's data.
    """
    user_profile = {
        "First_Name": "Joe",
        "Last_Name": "Moe",
        "Email_Address":"nomojoemoe@yafoo.com",
        "Phone_Number":"03030300303",
        "Relation to me":"brother",
    }
    # print(user_profile["First_Name"])
    print('\nScenario 1c: Dictionary with literal string interpolation')
    # items = user_profile.items()
    # print(items)
    # keys = user_profile.keys()
    # print(keys)
    values = user_profile.values()
    print(values)


# task 2:
def print_relative_profile():
    """
    Task 2 uses nested dictionaries to collect multiple users' data.
    """
    relatives_profile = {"close_kin": [{"First_Name": "Joe", "Last_Name": "Moe", "Relation_to_me": "brother", },
                                        {"First_Name": "Sue","Last_Name": "Moe", "Relation_to_me": "mother", },
                                       {"First_Name": "Boe", "Last_Name": "Moe", "Relation_to_me": "father", },
                                       ], }
    # values = {close_kin}.pop("Last_Name") #did not work
    # relatives_profile = relatives_profile{close_kin}.pop("Last_Name")
    # print('\nTask 2: Iterate through the list, printing first name and relationship')
    for _ in relatives_profile:
        print(relatives_profile["close_kin"],end="; ") #does not pop out Last name


