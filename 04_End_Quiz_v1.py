""" Added code to ask the user if they wanted to play again
"""

import random

QUESTIONS = [["Question 1 / What is number 1:", "Tahi"],
             ["Question 2 / What is number 2:", "Rua"],
             ["Question 3 / What is number 3:", "Toru"],
             ["Question 4 / What is number 4:", "Wha"],
             ["Question 5 / What is number 5:", "Rima"],
             ["Question 6 / What is number 6:", "Ono"],
             ["Question 7 / What is number 7:", "Whitu"],
             ["Question 8 / What is number 8:", "Waru"],
             ["Question 9 / What is number 9:", "Iwa"],
             ["Question 10 / What is number 10:", "Tekau"]]


# Functions go here
# Yes no checker function
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
        # Picking Random Number from selection
        question_number = random.randrange(len(questions))
        # Getting the correct answer
        answer = questions[question_number][1]
        user_answer = input(f"{questions[question_number][0]} ")
        del questions[question_number]
        if user_answer == answer:
            score += 1
            print("Correct")
        else:
            print("Incorrect")
    end_quiz(score)


# End Quiz function
def end_quiz(score):
    # Getting Final score
    print(f"You got {score}/10 questions correct")


end_quiz(score=0)


