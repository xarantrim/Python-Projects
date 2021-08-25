# Hangman

from replit import clear
import random
from Hangman_words import word_list

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# word_list = ["aardvark", "baboon", "camel"]
life = 0
i = 5
chosen_word = random.choice(word_list)
from Hangman_art import logo, stages

print(logo)
print(f'Pssst, the solution is {chosen_word}.')
display = []
wrong_answer = []
right_answer = []
answers = []
# for letter in chosen_word:
#     display += "_"

for letter in range(len(chosen_word)):
    display += "_"
print(' '.join(display))

while life < 6:
    guess = input("Please guess a letter\n").lower()
    clear()
    if guess in right_answer:
        print(f"You've already guessed {guess}")
        continue

    if not guess:
        print('Wrong! Empty String!')
        continue
    elif len(guess) > 1:
        print('Wrong Answer! Please only one char!')
        continue
    elif guess.isnumeric() or not guess.isalpha():
        print('Wrong Answer! Must be a char!')
        continue

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    # if guess in right_answer or wrong_answer:
    #     print(f'Char {guess} is already given! Try again!')
    #     continue

    if guess in chosen_word:
        right_answer.append(guess)

        # for index, c in enumerate(chosen_word):
        #     if c == guess:
        #         display[index] = guess
        #     break

    # if guess in chosen_word:
    #     for index, c in enumerate(chosen_word):
    #         if c == guess:
    #             display[index] = guess
    #         break

    if guess not in chosen_word:
        if life != 5:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(f"You still have {i} lives")
        wrong_answer.append(guess)
        life = life + 1
        i = i - 1
        if life == 6:
            print(f"You Lose!! The word was {chosen_word}")

    print(display)
    print(f"Your wrongs answers are:{wrong_answer}")
    print(f"Your rights answers are:{right_answer}")

    if "_" not in display:
        print("Congratulation!!You Won!!")
        break

    print(stages[life])
