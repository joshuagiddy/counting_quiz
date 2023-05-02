""" 01_yes_no_checker_v2
Improving the answer by making 'Yes' and 'No' works.
Also shows what answer you put into the program after"""


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

