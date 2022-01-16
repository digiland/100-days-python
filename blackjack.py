import os
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def deal_card(user, card_list):
    card = random.choice(card_list)
    user.append(card)


def calculate_score(user):
    score = sum(user)
    if len(user) == 2:
        if score == 21:
            return 'Blackjack!'

    elif score > 21 and 11 in user:
        user.remove(11)
        user.append(1)
        score = sum(user)
        return score

    return score


def compare():
    if user_score > dealer_score:
        return 'You win!'
    elif user_score == dealer_score:
        return 'Tie!'
    else:
        return 'You lose!'


def play():
    for _ in range(2):
        deal_card(dealer_cards, cards)
        deal_card(user_cards, cards)
    dealer_score = calculate_score(dealer_cards)
    user_score = calculate_score(user_cards)
    print('Dealer has: ' + str(dealer_cards) +
          ' for a score of: ' + str(dealer_score))

    while True:
        print('Your cards are: ' + str(user_cards) +
              ' for a score of: ' + str(user_score))
        choice = input('Do you want to hit or stay? ')
        if choice == 'hit':
            deal_card(user_cards, cards)
            user_score = calculate_score(user_cards)
            if user_score > 21:
                print('You busted!')
                break
        elif choice == 'stay':
            break
        else:
            print('Invalid choice!')
            continue

    print('Dealer has: ' + str(dealer_cards) +
          ' for a score of: ' + str(dealer_score))
    print(compare())


to_play = True

while to_play:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_cards = []
    user_cards = []
    dealer_score = 0
    user_score = 0
    clearConsole()
    print('Welcome to Blackjack!')
    play()
    to_play = input('Do you want to play again? (y/n) ')
    if to_play == 'n':
        to_play = False
