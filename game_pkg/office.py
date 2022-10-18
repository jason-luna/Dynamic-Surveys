import sys

# keep score of all characters
character_score = {"Michael": 0, "Jim": 0, "Pam": 0, "Dwight": 0, "Andy": 0, "Phyllis": 0, "Stanley": 0,
                   "Angela": 0, "Oscar": 0, "Kevin": 0, "Meredith": 0, "Creed": 0, "Toby": 0, "Kelly": 0, "Ryan": 0}

# questions, options, and character answers for quiz all in one dictionary
# {question1: [[possible option choice for user, character corresponding to option], ...], question2: [[option, character], [option, character], ...], ...}
q_and_a = {
    "What would you first spend your money on if you won the lottery?":  # question 1
    [["House", "Pam"], ["Yacht", "Andy"], ["Sports car", "Ryan"], [
        "Vacation", "Stanley"], ["Real Estate", "Oscar"], ["Gambling", "Kevin"]],
    "What would you do during an emergency?":  # question 2
    [["Panic", "Michael"], ["Remain calm", "Toby"], ["Take charge", "Dwight"], [
        "Pray", "Angela"], ["Help others remain calm", "Phyllis"], ["Nothing", "Creed"]],
    "What channel would you watch on TV?":  # question 3
    [["HGTV", "Pam"], ["Food Network", "Kevin"], ["ESPN", "Jim"], [
        "Discovery", "Andy"], ["Game Show Network", "Stanley"], ["MTV", "Kelly"]],
    "What would you do to pass the time at work?":  # question 4
    [["Knit", "Phyllis"], ["Puzzles", "Stanley"], ["Read a book", "Toby"], [
        "Play solitaire", "Meredith"], ["Go home", "Creed"], ["Gossip", "Kelly"]],
    "Choose a word your friends would use to describe you:":  # question 5
    [["Charming", "Jim"], ["Smart", "Oscar"], ["Stubborn", "Angela"], [
        "Loyal", "Dwight"], ["Quirky", "Andy"], ["Caring", "Phyllis"]],
    "At parties, when someone hands you a drink you…":  # question 6
    [["Drink it because everyone else is drinking", "Toby"], ["Chug/shotgun", "Meredith"], ["Hold it for the entirety of the party", "Oscar"],
        ["Drink it, and a couple more", "Kelly"], ["Never happened, parties are wack", "Angela"], ["Toss it because you are DD", "Pam"]],
    "What would be in your desk drawer?":  # question 7
    [["Change of clothes", "Kelly"], ["Natural disaster kit", "Dwight"], ["Books", "Toby"], [
        "Bottle of liquor", "Meredith"], ["Snacks/candy", "Kevin"], ["Office supplies", "Oscar"]],
    "What got you in trouble during high school?":  # question 8
    [["Disruptive behavior", "Michael"], ["Pranks", "Jim"], ["Not participating during PE", "Kevin"], [
        "Fighting", "Meredith"], ["Selling contraband", "Creed"], ["Skipping class", "Ryan"]],
    "What are you worst at dealing with?":  # question 9
    [["Speaking up", "Phyllis"], ["Feeling old", "Creed"], ["Rejection", "Ryan"], [
        "Saying no", "Pam"], ["Not being liked", "Michael"], ["Incompetence", "Angela"]],
    "How would you propose to your significant other?":  # question 10
    [["Family dinner", "Jim"], ["Flash mob", "Andy"], ["Elope in Vegas", "Ryan"], ["Grand gesture", "Michael"], ["From the comfort of your own home", "Stanley"], ["Scavenger Hunt", "Dwight"]]}

# bonus question; prompted only if tie-breaker needed
bonus_q = {
    "What color do you prefer to wear?":
    [["Black", "Michael"], ["Blue", "Jim"], ["Turquoise", "Pam"], ["Yellow", "Dwight"], ["White", "Andy"], ["Purple", "Phyllis"], ["Brown", "Stanley"],
     ["Gray", "Angela"], ["Gold", "Oscar"], ["Bronze", "Kevin"], ["Green", "Meredith"], ["Red", "Creed"], ["Beige", "Toby"], ["Pink", "Kelly"], ["Silver", "Ryan"]]}


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


def office_quiz():
    """
    Quiz game to determine what character from The Office your personality most closely matches.

    This function prompts questions and options for user input and tallies up score to find max character score.

    Returns
    -------
    str
        Character with max score
    """
    print("\nWelcome to The Office!")
    print("After answering a few personality questions, the character you most resemble will be determined!")
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
            choice = input("Select an option 1-6: ")
            if choice == "1":
                character_score[q_and_a[question][0][1]] += 1
                break
            elif choice == "2":
                character_score[q_and_a[question][1][1]] += 1
                break
            elif choice == "3":
                character_score[q_and_a[question][2][1]] += 1
                break
            elif choice == "4":
                character_score[q_and_a[question][3][1]] += 1
                break
            elif choice == "5":
                character_score[q_and_a[question][4][1]] += 1
                break
            elif choice == "6":
                character_score[q_and_a[question][5][1]] += 1
                break
            else:
                print("Invalid option. Please select an option 1-6")
        option_number = 1

    max_scores = [char for char, score in character_score.items()
                  if score == max(character_score.values())]

    if len(max_scores) > 1:
        print(f"\n{next(iter(bonus_q))}")
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
                        f"\nYour personality matches {bonus_answers[bonus_choice.title()]}!")
                    reset_score(character_score)
                    break
                else:
                    print(
                        "Invalid option. Please type an option provided in the question.")
    else:
        print(
            f"\nYour personality matches {max_scores[0]}!")
        reset_score(character_score)
