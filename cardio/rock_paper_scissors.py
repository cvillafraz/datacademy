import random


def prs(p1_choice):
    p2_choice = random.choice(['paper', 'rock', 'scissors'])

    if p1_choice == p2_choice:
        print('Tie, continue')
    elif (
        p1_choice == 'paper' and p2_choice == 'rock'
        or p1_choice == 'rock' and p2_choice == 'scissors'
        or p1_choice == 'scissors' and p2_choice == 'paper'
    ):
        return 'player 1'
    else:
        return 'player 2'


def run():
    scores = {
        'player 1': 0,
        'player 2': 0
    }
    print('Welcome player 1')
    while scores['player 1'] != 2 and scores['player 2'] != 2:
        p1_choice = input(
            'Choose between paper, rock or scissors (as written): ')
        winner = prs(p1_choice)
        scores[winner] += 1
        print(
            f"This round's winner is {winner}, the score is {scores['player 1']}-{scores['player 2']}")

    print(
        f"The winner is player {1 if scores['player 1'] > scores['player 2'] else  2}!")


if __name__ == "__main__":
    run()
