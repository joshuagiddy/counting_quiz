# Ask the student if they have played before.
instructions = input("Have you done this quiz before: ")
# If they say yes, print 'Program Continues'.
if instructions == "yes":
    print("program continues")
# If they say no, print 'Display Instructions'.
elif instructions == "no":
    print("Display Instructions")
# Otherwise - show error.
else:
    print("error, please answer 'yes' or 'no'")

