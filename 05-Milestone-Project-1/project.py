def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']

display(row1, row2, row3)

result = input("Please enter a value:")
# print(result)
# print(type(result))
result_int = int(result)

position_index = int(input("Choose an index postion:"))


def user_choice():
    # ? Variable
    # ?Initial
    choice = "WRONG"
    acceptable_range = range(0, 10)
    within_range = False
    # ? Two conditions to check
    # ? Digit or within_range==False
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10)")
        # ? digit check
        if choice.isdigit() == False:
            print("Sorry that is not a digit")
        # ? range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry,you are out of acceptable range(0-10)")
                within_range = False
    return int(choice)


user_choice()
