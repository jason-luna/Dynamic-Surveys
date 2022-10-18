import sys

# keep score of all houses
house_score = {"Gryffindor": 0, "Hufflepuff": 0,
               "Ravenclaw": 0, "Slytherin": 0}

# questions, options, and house answers for quiz all in one dictionary
# {question1: [[possible option choice for user, house corresponding to option], ...], question2: [[option, house], [option, house], ...], ...}

q_and_a = {
    "What element would you choose?":  # question 1
    [["Air", "Ravenclaw"], ["Water", "Slytherin"], [
        "Earth", "Hufflepuff"], ["Fire", "Gryffindor"]],
    "What state of matter is most appealing to you?":  # question 2
    [["Plasma", "Gryffindor"], ["Gas", "Ravenclaw"], [
        "Liquid", "Slytherin"], ["Solid", "Hufflepuff"]],
    "Choose a word your friends would use to describe you:":  # question 3
    [["Brave", "Gryffindor"], ["Resourceful", "Slytherin"],
        ["Smart", "Ravenclaw"], ["Loyal", "Hufflepuff"]],
    "What superpower would you choose?":  # question 4
    [["Night vision", "Hufflepuff"], ["Strength", "Gryffindor"],
        ["Speed", "Slytherin"], ["Flight", "Ravenclaw"]],
    "Who would you want to hang out with?":  # question 5
    [["Luna Lovegood", "Ravenclaw"], ["Cedric Diggory", "Hufflepuff"],
        ["Harry Potter", "Gryffindor"], ["Draco Malfoy", "Slytherin"]],
    "Where would you hang out at Hogwarts?":  # question 6
    [["Basement", "Hufflepuff"], ["Dungeon", "Slytherin"], [
        "Tower", "Gryffindor"], ["Common room", "Ravenclaw"]],
    "What house relic would you save first?":  # question 7
    [["Precious diadem", "Ravenclaw"], ["Silver locket", "Slytherin"],
        ["Goldern Cup", "Hufflepuff"], ["Magic sword", "Gryffindor"]],
    "Who would you want as a professor?":  # question 8
    [["Snape", "Slytherin"], ["Trelawney", "Ravenclaw"], [
        "Mcgonagall", "Gryffindor"], ["Sprout", "Hufflepuff"]],
    "Who would you haunt the halls with?":  # question 9
    [["The Fat Friar", "Hufflepuff"], ["The Bloody Baron", "Slytherin"], [
        "The Grey Lady", "Ravenclaw"], ["Nearly-Headless Nick", "Gryffindor"]],
    "What metal do you most favor?":  # question 10
    [["Silver", "Slytherin"], ["Bronze", "Ravenclaw"],
        ["Gold", "Gryffindor"], ["Lead", "Hufflepuff"]]
}

# bonus question; prompted only if tie-breaker needed
bonus_q = {
    "what color you look best in?":
    [["Red", "Gryffindor"], ["Yellow", "Hufflepuff"], ["Blue", "Ravenclaw"], ["Green", "Slytherin"]]}


def reset_score(score_dict):
    """
    Reset dictionary keeping score.

    This function resets the score to 0 for each character.

    Parameters
    ----------
    score_dict : dict
        Dictionary keeping score

    Returns
    -------
    dict
        Dictionary with values of 0
    """
    for char in score_dict:
        score_dict[char] = 0


def hogwarts_quiz():
    """
    Quiz game to determine what house from Harry Potter's Hogwarts a user would be placed in

    This function prompts questions and options for user input and tallies up score to find max house score.

    Returns
    -------
    str
        House with max score
    """
    print("\nWelcome Wizard! Let the sorting ceremony commence!")
    print("After answering a few questions, the Sorting Hat will decide your house!")
    print("Let's begin")

    question_number = 1
    option_number = 1
    for question, options in q_and_a.items():
        print(f"\nQuestion {question_number}) {question}")
        question_number += 1
        for option in options:
            print(f"{option_number}) {option[0]}")
            option_number += 1
        while True:
            choice = input("Select an option 1-4: ")
            if choice == "1":
                house_score[q_and_a[question][0][1]] += 1
                break
            elif choice == "2":
                house_score[q_and_a[question][1][1]] += 1
                break
            elif choice == "3":
                house_score[q_and_a[question][2][1]] += 1
                break
            elif choice == "4":
                house_score[q_and_a[question][3][1]] += 1
                break
            else:
                print("Invalid option. Please select an option 1-4")
        option_number = 1

    max_scores = [house for house, score in house_score.items()
                  if score == max(house_score.values())]

    if len(max_scores) > 1:
        print(f"\nThe sorting hat would like to know {next(iter(bonus_q))}")
        bonus_answers = {}
        for options in bonus_q.values():
            for option in options:
                if option[1] in max_scores:
                    print(option[0])
                    bonus_answers[option[0]] = option[1]
            while True:
                bonus_choice = input("Type your answer: ")
                if bonus_choice.title() in bonus_answers:
                    print(
                        f"\nThe sorting hat has placed you in the house of {bonus_answers[bonus_choice.title()]}!")
                    reset_score(house_score)
                    break
                else:
                    print(
                        "Invalid option. Please type an option provided in the question.")
    else:
        print(
            f"\nThe sorting hat has placed you in the house of {max_scores[0]}!")
        reset_score(house_score)
