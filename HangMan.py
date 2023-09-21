import random
import hangman_art
import hangman_words

print(hangman_art.logo)

lives = 6


chosen_word = random.choice(hangman_words.word_list)
#print(f'Chosen word -> {chosen_word}')

chosen_word_list = []
chosen_word_length = len(chosen_word)
for _ in range(chosen_word_length):
  chosen_word_list += "_"

print(chosen_word_list)

while "_" in chosen_word_list and lives > 0:
  user_alpha = input("Guess a letter -> \n").lower()
  if user_alpha in chosen_word_list:
      print(f"'{user_alpha}' letter already used")
  if user_alpha not in chosen_word:
    print(f"{user_alpha} is not present. You lose a live")
    lives-=1
  for position in range(chosen_word_length):
    letter = chosen_word[position]
    if user_alpha == letter:
      chosen_word_list[position] = letter
  print(chosen_word_list)
  print(hangman_art.stages[lives])

if lives == 0:
  print("You lost!!!")
  print(f"The word is {chosen_word}")
else:
  print("You won!!!")