"""01_yes_no_checker_v4
based on 01_yes_no_checker_v4 but put into a function
"""


# Function goes here
def yes_no(question_text):
    while True:

        # Ask the user if they have played before.
        answer = input(question_text).lower()

        # If they say yes, print 'Program Continues'.
        if answer == "yes" or answer == "Yes":
            return answer

        # If they say no, output 'Display Instructions'.
        elif answer == "no" or answer == "No":
            return answer

        # Otherwise - show error.
        else:
            print("error, please answer 'yes' or 'no'")


def instructions():
    print("*** How Quiz Works ***")
    print()
    print("The instructions of the quiz will go here")
    print("Program continues")
    print()

# Main routine goes here


question = yes_no("Have you done this quiz before? ")

if question == "No" or "no":
    instructions()







