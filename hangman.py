import random

words = ["PYTHON","JAVA","PROGRAM","CODING","COMPUTER"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("===========================================")
print("              HANGMAN GAME                 ")
print("===========================================")

print("Welcome to our HANGMAN GAME")

name = input("What is your name: ")
if not name:
    name = "Player"

print(f"Hello  {name} , let's play the HANGMAN GAME!" )

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "
        else:
            display_word = display_word + "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:",wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter:").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses = wrong_guesses + 1
        print("Wrong guess!")

    if wrong_guesses == max_wrong_guesses:
        print("Game over! You lost.")
        print("The secret word was:", secret_word)
            

