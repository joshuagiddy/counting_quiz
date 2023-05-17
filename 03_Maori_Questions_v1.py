""" Added code to ask a random question from the question list
then remove that question and answer from the list
"""


import random

QUESTIONS = [["question 1", "answer 1"],
             ["question 2", "answer 2"],
             ["question 3", "answer 3"],
             ["question 4", "answer 4"],
             ["question 5", "answer 5"],
             ["question 6", "answer 6"],
             ["question 7", "answer 7"],
             ["question 8", "answer 8"],
             ["question 9", "answer 9"],
             ["question 10", "answer 10"]]


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


def question(questions, score):
    while len(questions) != 0:
        question_number = random.randrange(len(questions))
        answer = questions[question_number][1]
        user_answer = input(f"{questions[question_number][0]} ")
        del questions[question_number]
