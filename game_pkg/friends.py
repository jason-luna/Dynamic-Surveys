import sys

score = 0

# questions, options, and answer idicator for quiz all in one dictionary
# {question1: [[possible option choice for user, yes or no for correct answer], ...], question2: [[option, Y or N], [option, Y or N], ...], ...}
q_and_a = {
    "What are Ross and Monica's parent's names?":  # question 1
    [["Jack and Judy", "Yes"], ["John and Ruth", "No"], [
        "Matthew and Linda", "No"], ["David and Courtney", "No"]],
    "What is Phoebe's twin sister's name?":  # question 2
    [["Jesse", "No"], ["Ursula", "Yes"], [
        "Arial", "No"], ["Emily", "No"]],
    "What does Ross dress up as to teach Ben about Christmas and Hanukkah?":  # question 3
    [["The Holiday Elephant", "No"], ["The Holiday Sheep", "No"],
        ["The Holiday Armadillo", "Yes"], ["The Holiday Worm", "No"]],
    "What hangs on Monica's purple door?":  # question 4
    [["A coat hook", "No"], ["A yellow picture frame", "Yes"],
        ["A family portrait", "No"], ["An ornament", "No"]],
    "How many times did Ross get married?":  # question 5
    [["1", "No"], ["2", "No"], ["3", "Yes"], ["4", "No"]],
    "What kind of uniform does Joey wear to Chandler and Monica's wedding?":  # question 6
    [["Soldier", "Yes"], ["Police", "No"], [
        "Sailor", "No"], ["Pilot", "No"]],
    "What is Janice most likely to say?":  # question 7
    [["That's what she said!", "No"], ["No way, Jose!", "No"],
        ["Bing bong!", "No"], ["Oh... my... God!", "Yes"]],
    "What was Chandler's job?":  # question 8
    [["Comedian", "No"], ["Data processor", "Yes"], [
        "Financial advisor", "No"], ["Accountant", "No"]],
    "What song is Phoebe best known for?":  # question 9
    [["Smelly Rat", "No"], ["Smelly Car", "No"], [
        "Smelly Sock", "No"], ["Smelly Cat", "Yes"]],
    "Who wears the turkey on their head?":  # question 10
    [["Chandler", "No"], ["Monica", "Yes"],
        ["Phoebe", "No"], ["Joey", "No"]]}


def friends_quiz():
    """
    Trivia quiz game for the show "Friends".

    This function prompts questions and options for user input and tallies up score to determine how familiar user is with the show.

    Returns
    -------
    str
        User score and rating
    """
    global score
    print("\nWelcome!")
    print("How well do you know F.R.I.E.N.D.S? This quiz will determine whether you are a true fan or just a fraud")
    print("Let's begin")

    question_number = 1
    option_number = 1
    option_answers = {}
    answer_key = []
    for question, options in q_and_a.items():
        print(f"\nQuestion {question_number}) {question}")
        question_number += 1
        for option in options:
            print(f"{option_number}) {option[0]}")
            option_answers[str(option_number)] = option[1]
            if option[1] == "Yes":
                answer_key.append(f"{question_number-1}) {option[0]}")
            option_number += 1
        while True:
            choice = input("Select an option 1-4: ")
            if choice in option_answers:
                if option_answers[choice].title() == "Yes":
                    score += 1
                    break
                else:
                    break
            else:
                print("Invalid option. Please select an option 1-4")
        option_number = 1

    print(f"\nYou scored a {score}/10")
    if score >= 10:
        print("Wow! A perfect score! You must be a true Friend!")
        score = 0
    elif score >= 7 and score < 10:
        print("Great job! Those Friends marathons paid off!")
        score = 0
    elif score >= 4 and score < 7:
        print("Good job! You must have grew up in the 90s!")
        score = 0
    else:
        print("Oof. Have you ever watched this show?!")
        score = 0
    while True:
        see_answers = input("Would you like to see the answer key? (Y/N): ")
        if see_answers.lower() == "y":
            for answer in answer_key:
                print(answer)
            break
        elif see_answers.lower() == "n":
            break
        else:
            print("Invalid option. Please select Y or N.")
