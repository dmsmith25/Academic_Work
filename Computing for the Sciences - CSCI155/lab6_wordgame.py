"""
CSCI 150 Lab 6

Name: Dean Smith
Section: V

Creativity:

- Uses a pyramid to represent how many incorrect guesses are remaining through
the levels of pyramid remaining (line 112)

- If guessed letter if longer than one character then it prompts the user for
another letter (line 120)

"""
from random import randint


def set_to_string(input_set):
    """
    This function takes a set as a parameter and returns
    all of the items in the set as one string.
    Inputs: input_set
    """
    string = ''
    for item in input_set:
        item = item.upper()
        string = string + item + ' '
        
    return string



def read_words(filename):
    """
    This function takes in a file of words as a parameter and returns
    a list of all the words in the file.
    Inputs: filename (str)
    """
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            word_list.append(line.strip())
            
            
    return word_list



def insert_letter(letter, underscored_word, word):
    """
    This function takes a letter guessed by the user, how much of the
    letter the user has guessed correctly, and the word they are trying
    to guess and uses this to then fill in the blanks of the word where the letter
    is.
    Inputs: letter (str), correctly guessed letters with blanks (str), the correct word (str)
    """
    letter = letter.lower() # for tests both the letter and word need to be returned in lowercase
    word = word.lower()
    new_underscored_word = ''
    for i in range(len(word)):
        if letter == word[i]:
            new_underscored_word += letter

        else:
            new_underscored_word += underscored_word[i]
            
    return new_underscored_word


def hidden_word(word):
    """
    This funciton takes a word and returns the amount of letters in the word
    as underscores.
    Inputs: word (str)
    """
    new_word = ''
    for i in range(len(word)):
        new_word = new_word + '_'
        
    return new_word


def play_wordgame(filename, guesses_allowed = 7):
    """
    This function prompts the user for a file of words and the amount of guesses
    they want before it starts a game of selecting a random word from the file
    and having the user try to guess the letters in the word. The user has the input
    amount of incorrect guesses to get the word right or they will lose.
    Inputs: word file (string), guesses allowed (int)
    """
    
    guesses_left = guesses_allowed
    
    #uses read_words function
    words_available = read_words(filename)
    chosen_word = (words_available[randint(0, len(words_available) - 1)]).upper()
    
    correct_letters = set(chosen_word)
    
    
    guessed_letters = set()
    underscored_word = hidden_word(chosen_word)
    
    
    while correct_letters.intersection(guessed_letters) != correct_letters:
        print('--------------------')
        print('Guessed letters: ' + set_to_string(guessed_letters)) #uses set string function
        print('Incorrect guesses left: ')
        print('\n')
        # for pyramid to represent incorrect guesses remaining
        for guess in range(1, guesses_left + 1):
            print((' ' * (guesses_left - guess)) + ('/ ') + ('| ' * (guess - 1)) + ('\\'))
            
        print('\n')
        print('Word: ' + underscored_word)
        print('\n')
        
        guessed_letter = input('Guess a letter: ').upper()
        while len(guessed_letter) > 1:
            guessed_letter = input('Guess a letter: ').upper()
            
            
        if not (guessed_letter in guessed_letters):    
            if not (guessed_letter in correct_letters):
                if guesses_left == 0:
                    guessed_letters = correct_letters
                guesses_left = guesses_left - 1

            
            else:
                # uses insert_letter function
                underscored_word = insert_letter(guessed_letter, underscored_word, chosen_word)
                
            guessed_letters.add(guessed_letter)

        
      
    if guesses_left > 0:
        print('You win!')
        print('The word was: ' + chosen_word.lower())
        print('You guessed it with ' + str(guesses_allowed - guesses_left) + ' incorrect guesses')
        
    
    else:
        print('The word was: ' + chosen_word.lower())
        print('Better luck next time!')
    
    
    
        
        
    
    
    
    


if __name__ == '__main__':
    file_of_words = input('File of words (no parentheses): ')
    num_guesses = int(input('Guesses allowed (int): '))
    play_wordgame(file_of_words, num_guesses)
