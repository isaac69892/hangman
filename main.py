import random
from replit import clear
from hangman_images import starting_image, lives_images, lose_image, win_image
from hangman_strings import word_list

is_game_over = False
num_lives = len(lives_images) - 1

# Step 1: Print the starting_image onto console when we start the game
print(starting_image)
# Step 2: Choose a word from word_list to be mystery word for hangman game
word_to_guess = random.choice(word_list)
print(word_to_guess)
# Step 3: Show clue to player
word_length = len(word_to_guess)
print(word_length)

underscores = []
for i in range(word_length):
  underscores.append("_")

print(' '.join(underscores))
# Step 4: Get User to guess letter
while not is_game_over:
  guess = input("guess a letter").lower()

  clear()
  
  while (len(guess) != 1 or not guess.isalpha()):
    guess = input("Enter a valid letter").lower()
    
  # Step 5: Check if Letter guessed is in Mystery Word
  for i in range(word_length):
    if word_to_guess[i] == guess:
      underscores[i] = guess

  if guess in word_to_guess:
      print(" ".join(underscores))
  
  # Step 6: Check if Letter guessed is not in Mystery Word
  if guess not in word_to_guess:
    num_lives -= 1
    print("you have lost a life nobby")
  
    print(lives_images[num_lives])
  # Step 7: Check if Player won or lost
  
      #Check player has won
  if "_" not in underscores:
    is_game_over = True
    print(win_image)
  
  if num_lives == 0:
    is_game_over = True
    print(lose_image) 
  
    
  # Enclose Steps 4 to 7 in while loop so long as game is not ove
  