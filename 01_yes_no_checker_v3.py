""" 01_yes_no_checker_v3
Creating the 01_yes_no_checker_v2 into a loop"""

instructions = ""
while instructions != "x":
    instructions = input("Have you done this quiz before: ")
    # If they say yes, print 'Program Continues'.
    if instructions == "yes" or instructions == "Yes":
        print("program continues")
    # If they say no, print 'Display Instructions'.
    elif instructions == "no" or instructions == "No":
        print("Display Instructions")
    # Otherwise - show error.
    else:
        print("error, please answer 'yes' or 'no'")
    # This will show the answer they have entered.
    print(f"You have entered '{instructions}'")



