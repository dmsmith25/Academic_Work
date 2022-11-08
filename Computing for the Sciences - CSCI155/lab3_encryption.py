"""
CS 150 Lab 3

Name: Dean Smith
Section: V

Creativity: 

- Created shift function (line 186)
- Created my_encrypt (line 201) and my_decrypt (line 217)
"""

from random import randint, seed

ALPHABET = "abcdefghijklmnopqrstuvwxyz "

#---------------------------------------------------------
# Fools functions


# TODO: Write your fools function(s) here

def fools_encrypt(message):
    """
    This function takes an input message and translates it so that each
    character is written 3 times. Can be decrypted with fools_decrypt function
    Inputs: Message (string)
    """
    translation = ''
    # use for loop for each character of the message
    for c in message:
        translation = translation + (c * 3) # each character gets printed 3 times
        
    return translation



def fools_decrypt(message):
    """
    This function takes an input message from the fools_encrypt function
    and translates it back to the original message.
    Inputs: Message (string)
    """
    translation = ''
    translation = translation + message[::3] # prints every 3rd character
        
    return translation


#---------------------------------------------------------
# Caesar's method

def shift_letter(letter, num):
    """
    Shifts a letter up num places in the alphabet with
    wraparound.

    Args:
        letter: A single character
        num: Integer distance to shift letter

    Returns:
        Character in ALPHABET num distance from letter
    """
    # Get the index of the current letter
    index = ALPHABET.find(letter)
    # We use the mod operator (%) for wraparound
    return ALPHABET[(index + num) % len(ALPHABET)]


# TODO: Write your caesar_encrypt function here

def caesar_encrypt(message, shift):
    """
    This function takes an input message and translates it by using the shift_letter
    function to replace each character in the message with the character 'shift' places
    above them, shift is an input.
    Inputs: Message (string), Shift (int)
    """
    translation = ''
    # for loop for each index in message
    for c in range(len(message)):
        translation = translation + shift_letter(message[c], shift) # uses shift_letter functino
        
    return(translation)

#---------------------------------------------------------
# Substitution cipher

def splice(message, letter):
    """
    Splices out letter from message and returns the 
    remaining message. letter must occur exactly ONCE in
    the message.
    
    For example:
    >>> splice("abcdefg", "f")
    'abcdeg'

    Args:
        message: String
        letter: A string to be removed from message

    Returns:
        String message with letter removed.
    """
    
    # TODO: fill in the details of this function
    
    translation = ''
    
    message_index = message.find(letter)
    
    #includes all letters in message except input letter
    translation = translation + message[:message_index] + message[(message_index + 1):] 
        
    return translation




def keygen(password):
    """
    Given a string password, generates a new random key.
    A key consists of a random ordering of the letters in
    ALPHABET.

    Args:
        password: String password used to generate key

    Return:
        Key string
    """
    remaining = ALPHABET
    key = ""
    
    seed(password)
    
    for dummy in range(len(ALPHABET)):
        index = randint(0, len(remaining)-1)
        next_letter = remaining[index]
        key = key + next_letter
        remaining = splice(remaining, next_letter)
    
    return key
    
    
    
    
# TODO: Fill in your substitution functions here

def subst_encrypt(message, key):
    """
    This function takes a message and encrypts it using a specific key. The same message
    with the same key will give the same translation.
    Inputs: message (string), key (string)
    """
    translation = ''
    # for loop for all indecies of message
    for c in range(len(message)):
        # Takes the letter at place c in message and finds the index for that letter in ALPHABET and finds the letter for that index in key
        translation = translation + key[ALPHABET.find(message[c])]
        
    return translation




def subst_decrypt(message, key):
    """
    This function takes the message encrypted in the subst_encrypt function and decrypts it
    back to the original message using the same input key as the subst_encrypt function.
    Inputs: message (string), key (string)
    """
    translation = ''
    # for loop for all indecies of message
    for c in range(len(message)):
        # Takes the letter at place c in message and finds the index for that letter in key and finds the letter for that index in ALPHABET
        translation = translation + ALPHABET[key.find(message[c])] 
        
    return translation




def shift(number):
    """
    This function creates a string using the ALPHABET constant and shifts the letters over
    'number' letters which is inputed by the user.
    Input: number (int)
    """
    real_number = number % 27 #so that number can be equal to more than 27
    translation = ''
    translation = translation + ALPHABET[real_number:] + ALPHABET[:real_number] #lists alphabet starting from the index input number
    
    return translation




def my_encrypt(message, key):
    """
    This function encrypts an input message to generate a string of every letter ordered by even indexes first then odd indexes.
    Inputs: message (string), key (str)
    """
    real_key = ''
    real_key = real_key + key[::2] + key [1::2] # even then odd indexes are put into order
    translation = ''
    for c in message:
        translation = translation + real_key[ALPHABET.find(c)] # finds the index of the character in ALPHABET and finds the letter using the index in key
    return translation





def my_decrypt(message, key):
    """
    This function decrypts the message given by the subst_encrypt function using the same input key
    as the subst_encrypt function to give the original message.
    Inputs: message (string), key (str)
    """
    real_key = ''
    real_key = real_key + key[::2] + key [1::2] # even then odd indexes are put into order
    translation = ''
    # for loop for each character in message
    for c in message:
        translation = translation + ALPHABET[real_key.find(c)] # finds the index of the character in key and finds the letter using that index in ALPHABET
        
    return translation


        

    


    

