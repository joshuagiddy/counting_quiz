""" Added code to check if the user entered the correct answer, then print whether they were correct or not,
and increase the score if they were correct
"""


import random

QUESTIONS = [["Question 1:", "Tahi"],
             ["Question 2:", "Rua"],
             ["Question 3:", "Toru"],
             ["Question 4:", "Wha"],
             ["Question 5:", "Rima"],
             ["Question 6:", "Ono"],
             ["Question 7:", "Whitu"],
             ["Question 8:", "Waru"],
             ["Question 9:", "Iwa"],
             ["Question 10:", "Tekau"]]



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


# Instructions Function
def instructions():
    print("*** How Quiz Works ***")
    print()
    print("The instructions of the quiz will go here")
    print("Program continues")
    print()


# Questions Function
def question(questions, score):
    while len(questions) != 0:
        # Getting random Question
        question_number = random.randrange(len(questions))

        # Getting Correct Answer
        answer = questions[question_number][1]

        # Displaying Answer
        user_answer = input(f"{questions[question_number][0]} ")
        del questions[question_number]

        # If user gets it correct
        if user_answer == answer:
            score += 1
            print("Correct")
        # If user gets it incorrect
        else:
            print("Incorrect")


question(QUESTIONS, 0)
