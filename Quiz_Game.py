import math
print("Hello and welcome to my quiz game!")

while True:
    play = input("Do you want to play?: (y/n)").lower()
    if play == "y":
        print("Lets play!")
        break
    elif play == "n":
        print("Goodbye")
        quit()
    else:
        print("Invalid input. Please enter the letter y or n")
        continue

while True:
    count = 0
    question1 = input("Which country has the biggest population? ").lower()
    if question1 == "china":
        count = count + 1
        print("Correct!")
    else:
        print("You got it wrong")

    while True:
        question2 = input("What is 2x2? ")
        if question2.isdigit():
            if question2 == "4":
                count = count + 1
                print("Correct")
                break
            else:
                print("You got it wrong")
                break

        else:
            print("Please enter a digit!")
            continue

    question3 = input("In which month does Malaysian celebrate Merdeka?").lower()
    if question3 == "august":
        count = count + 1
        print("Correct")
    else:
        print("You got it wrong")

    print("You got", count, "questions correct")
    score = (count / 3) * 100
    format_score = "{:.2f}".format(score)
    print("Your score is", str(format_score), "%")

    if count > 1:
        print('Congratulations!')
    else:
        passing = input('Do you want to try again until you pass?(y/n): ').lower()
        if passing == 'y':
            continue
        else:
            print("Thank you for playing")
            break

