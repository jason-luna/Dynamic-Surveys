import sys
from game_pkg import office, hogwarts, friends
quiz = ""
play = True


def main_menu():
    """
    Main Menu with all quizzes available to take

    This function prints the main menu containing quiz choices and allows user to choose among options

    Returns
    -------
    func
        Quiz selected to take
    """
    global quiz
    print("\n------------------Main Menu------------------")
    print("Quizzes available to take:")
    print("1) Which Character From \"The Office\" Are You?")
    print("2) Which Hogwarts House Do you Belong In?")
    print("3) Are you a true fan of \"Friends\"?")
    print("---------------------------------------------")
    while True:
        choice = input("Which quiz would you like to take? (or q to quit): ")
        if choice == "1":
            office.office_quiz()
            quiz = "office"
            break
        elif choice == "2":
            hogwarts.hogwarts_quiz()
            quiz = "hogwarts"
            break
        elif choice == "3":
            friends.friends_quiz()
            quiz = "friends"
            break
        elif choice.lower() == "q":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please select an option from the menu")
    while play:
        play_again()


def play_again():
    """
    Prompts options for user to play again or return to main menu

    This function takes user input to call same quiz function again, call main menu function, or quit program

    Returns
    -------
    func
        Quiz or main menu
    """
    print("\n----------------Game Over----------------")
    print("1) Take quiz again")
    print("2) Take another quiz (return to main menu)")
    print("-----------------------------------------")
    game_over = input("Choose an option (or q to quit): ")
    while True:
        if game_over == "1":
            if quiz == "office":
                office.office_quiz()
                break
            elif quiz == "hogwarts":
                hogwarts.hogwarts_quiz()
                break
            elif quiz == "friends":
                friends.friends_quiz()
                break
        elif game_over == "2":
            main_menu()
            break
        elif game_over.lower() == "q":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please select an option from the menu")


# Play
print("Welcome!")
print(
    "Have you ever wondered if you were more a Jim or a Dwight, what colors you would sport at Howarts, or if you are a true fan of Friends?")
print("Take a quiz and find out!")
main_menu()
