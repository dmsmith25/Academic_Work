alphabet = 'abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz '


def decipher(message, shift):
    translation = ''
    for c in range(len(message)):
        translation = translation + alphabet[(alphabet.index(message[c]) + shift)]
        
    return(translation)


def decrpyt(message, shift):
    translation = ''
    for c in range(len(message)):
        translation = translation + alphabet[(alphabet.index(message[c]) - shift)]
        
    return(translation)

set_two = 'hvieksyrbdajqwncxmgufltp ozhvieksyrbdajqwncxmgufltp ozhvieksyrbdajqwncxmgufltp ozhvieksyrbdajqwncxmgufltp oz'

def decrypt_new(message):
    translation = ''
    for c in range(len(message)):
        translation = translation + set_two[alphabet.index(message[c])]
        
    return translation