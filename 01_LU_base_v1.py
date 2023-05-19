""" Added code to ask the user if they wanted to play again
"""

import random

QUESTIONS = [["Question 1 = What is number 1:", "Tahi"],
             ["Question 2 = What is number 2:", "Rua"],
             ["Question 3 = What is number 3:", "Toru"],
             ["Question 4 = What is number 4:", "Wha"],
             ["Question 5 = What is number 5:", "Rima"],
             ["Question 6 = What is number 6:", "Ono"],
             ["Question 7 = What is number 7:", "Whitu"],
             ["Question 8 = What is number 8:", "Waru"],
             ["Question 9 = What is number 9:", "Iwa"],
             ["Question 10 = What is number 10:", "Tekau"]]
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

#Instructions Function
def instructions():
    print()
    print(formatter("*", "How Quiz Works"))
    print()
    print("This is a Quiz to see how well your Te Reo Māori is!")
    print()
    print("You will be displayed a number, picked from random from 1 - 10")
    print()
    print("You will have to answer the picked number and type the correct Māori WORD")
    print()
    print("After the 10 questions it will say how well you did!")
    print()
    print("Enjoy!")
    print()
    print("-" * 50)
    print()

# Questions Function
def question(questions, score):
    while len(questions) != 0:
        # Picking Random Number from selection
        question_number = random.randrange(len(questions))

        # Getting the correct answer
        answer = questions[question_number][1]

        # Displaying Answer
        user_answer = input(f"{questions[question_number][0]} ")
        del questions[question_number]

        # If user gets Correct Answer
        if user_answer == answer:
            score += 1
            print(formatter("$", "Correct"))

        # If user gets Wrong Answer
        else:
            print(formatter("X", "Incorrect"))
    end_quiz(score)


# end quiz function
def end_quiz(score):

    # Telling user the score
    print(f"You got {score}/10 questions correct")

    # Asking if they want to play again
    play_again = yes_no("Would you like to play again? (Yes/No) ")

    # If user says yes, restart program
    if play_again == "yes":
        question(QUESTIONS, 0)

    # If no then sends thank you message
    elif play_again == "no":
        print(formatter("!", "Thanks for playing"))
    else:
        print(formatter("#", "Invalid Input"))


# Formatter function
def formatter(symbol, text):
    # Getting width of sides
    sides = symbol * 3
    # putting the symbol on the text sides
    formatted_text = f"{sides} {text} {sides}"
    # Getting the symbol above and below the text
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
welcome_message = print(formatter("*", "Welcome to my Maori Quiz"))
played_before = yes_no("Have you done this quiz before? ")

if played_before == "no":
    instructions()
    question(QUESTIONS, 0)
else:
    question(QUESTIONS, 0)


