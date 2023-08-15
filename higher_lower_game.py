from art import logo, vs
from game_data import data
from random import randint


def play_game(persona1, persona2):
    """Takes in the form of a dictionary, data of the two person and returns 1 if the user made a winning choice """
    print(f"\033[96mCompare A:\033[0m {persona1['name']}, a {persona1['description']}, from {persona1['country']}.")
    print(vs)
    print(f"\033[96mAgainst B:\033[0m {persona2['name']}, a {persona2['description']}, from {persona2['country']}.")
    answer = compare_A_B(persona1, persona2)  # Compare the numer of followers of the two people
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice.lower() == answer.lower():
        return [1, answer]  # Return 1 for correct choice along with the answer that is correct
    else:
        return [0]  # Return 0 for wrong choice


def compare_A_B(persona1, persona2):
    """
    Compare followers of the two persons
    :param persona1: Dictionary of person1
    :param persona2: Dictionary of person1
    :return: 'A' if person1 has more followers than person2, and 'B' for vice versa
    """
    follower_count_1 = persona1['follower_count']
    follower_count_2 = persona2['follower_count']
    if follower_count_1 > follower_count_2:
        return 'A'
    else:
        return 'B'


def pick_account(dataset):
    """
    randomly pick an person from the dataset
    :param dataset: list of dictionaries of all data
    :return: a dictionary
    """
    random_int = randint(0, len(dataset) - 1)
    temp = dataset[random_int]
    del dataset[
        random_int]  # delete the entry from the instance of dataset so that the same entry doesn't get picked again.
    return temp


should_continue = 1

print(logo)
persona1 = pick_account(dataset=data)
persona2 = pick_account(dataset=data)
score = 0
while should_continue == 1:
    result = play_game(persona1, persona2)
    if result[0] == 0:  # if the user made a wrong choice
        should_continue = 0
        print("\033[91mSorry, that's wrong, you lose.\033[96m")
    else:  # if the choice was correct
        score += 1
        print(f"\033[92mYou're right! Current Score: {score}\033[0m")
        if result[1] == 'A':
            persona2 = pick_account(dataset=data)
        else:
            persona1 = persona2  # Switch the losing instagram account with the winner
            persona2 = pick_account(dataset=data)
print(f"Game Over! your final score is {score}")
