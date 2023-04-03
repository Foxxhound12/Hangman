#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]
hangman_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


chosen_word = random.choice(word_list)
empty_lines = []
for letter in chosen_word:
    empty_lines.append("_")
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

#print(empty_lines)

life_count = 6
x=0

chosen_word_list = list(chosen_word)
while life_count > 0:

    guess = input("Guess a character: ").lower()
    if guess in empty_lines:
        print("You already guessed that letter!")

    elif guess in chosen_word:

        for letter in chosen_word:
            if guess == letter:
                empty_lines[x] = letter
            x +=1
    else:
        life_count -= 1
    print(hangman_art[6-life_count])
    print(empty_lines)
    print(life_count)
    x=0

    #print(chosen_word_list)
    if life_count == 0:
        print("Game Over, you lost!")
    if empty_lines == chosen_word_list:
        print("Congratulations, you won!")
        break

