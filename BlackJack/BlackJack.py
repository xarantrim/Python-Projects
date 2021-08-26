# Black Jack

import random
from BlackJack_art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You Lose, Dealer has Blackjack!"
    elif user_score == 0:
        return "You Win with a Blackjack!!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!!"
    elif user_score > computer_score:
        return "You win!!"
    else:
        return "You lose!"


def start_game():
    print(logo)

    user_cards = []
    computer_cards = []
    not_game_over = True

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            not_game_over = False
        else:
            user_get_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_get_card == "y":
                user_cards.append(deal_card())
            elif user_get_card == 'n':
                not_game_over = False
            else:
                print("Please choose only 'y' or 'n'")
                continue

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


start = True
while start:
    x = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if x == 'y':
        start_game()
    elif x == 'n':
        print("Bye Bye!!")
        start = False
    else:
        print("Please choose only 'y' or 'n'")
        continue
