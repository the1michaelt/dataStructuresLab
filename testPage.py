months=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")


def month_of_Pi(months):
    """
    Task 1a: Tuple is the best data strategy for months of the year which will never change.

    Big O notation is linear, O(n).
    """
    count= 0
    stop= len(months)-1
    while count <= stop:
        Pi= 3.14
        Pi= int(Pi)
        if count == (Pi-1): 
            print('Scenario 1a: Tuple. The month of Pi is {}.'.format(months[count]))
            break
        else:
            count+=1

# # def print_month_of_pi():
# #       months = ("January", "February", "March", "April")
# #       pi = 3.14
# #       correct_month_number = int(pi)
# #       print(f"The Pi Month is {months[correct_month_number - 1]}")


month_of_Pi(months)


def print_favorite_fruits_veggies():
    """
    Task 1b: Set is the best data strategy for SEPARATE SOURCES, collated together.

    Add two favorite fruits and two favorite veggies, print the aggregated list.
    """
    two_favorite_fruits = {"strawberries", "raspberries"}
    two_favorite_vegetables = {"eggplant", "carrots"}
    five_fruits_or_vegetables = {"passionfruit"}

    five_fruits_or_vegetables.update(two_favorite_fruits)
    five_fruits_or_vegetables.update(two_favorite_vegetables)
    print('\nScenario 1b: Set')
   
    for produce in five_fruits_or_vegetables:
        print(produce)

print_favorite_fruits_veggies()


# user_profile = {}. Use literal string interpolation to print the user’s profile information to the console.
# The profile should consist of the following information:
def print_profile():
    user_profile = {
        "First_Name": "Joe",
        "Last_Name": "Moe",
        "Email_Address":"nomojoemoe@yafoo.com",
        "Phone_Number":"03030300303",
    }
    # print(user_profile["First_Name"])
    print('\nScenario 1c: Dictionary')
    for x in user_profile.values():
        print(x)
    
print_profile()

