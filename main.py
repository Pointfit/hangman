import random
import hangman_words
import hangman_art
from replit import clear

chosen_word = random.choice(hangman_words.word_list)
lives = 6
print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for n in chosen_word:
  display += "_"

while "_" in display and lives != 0:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print(f"You already guessed {guess}")
    if guess in chosen_word:
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                display[n] = guess
    else:
        lives -= 1
        print(f"{guess} is not in the word.")
    print(display)
    print(hangman_art.stages[lives])
if lives == 0:
    print("You lose")
else:
    print("You win")