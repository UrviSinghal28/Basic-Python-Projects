import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed

    lives = 7

    while len(word_letter) > 0 and lives > 0: #getting user input
        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        print(lives_visual_dict[lives])
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)
            
            if user_letter in word_letter:
                word_letter.remove(user_letter)

            else:
                lives -= 1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nInvalid character. Please try again.')

    if lives == 0:
        print('You died, sorry. The word was', word)
        print(lives_visual_dict[lives])
    
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()
