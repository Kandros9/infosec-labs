from getpass import getpass
import string

words = ['worship', 'outreach', 'luck']
alphabet = string.ascii_lowercase


def get_first_and_second_letter():
    word = words[1]
    old_letter = word[0]
    if old_letter == 'z':
        new_letter1 = 'a'
        new_letter2 = 'b'
    elif old_letter == 'y':
        new_letter1 = 'z'
        new_letter2 = 'a'
    else:
        old_index = alphabet.find(old_letter)
        new_letter1 = alphabet[old_index + 1]
        new_letter2 = alphabet[old_index + 2]
    return new_letter1 + new_letter2


def get_third_letter():
    word = words[1]
    old_letter = word[4]
    if old_letter == 'a':
        new_letter = 'z'
    else:
        old_index = alphabet.find(old_letter)
        new_letter = alphabet[old_index - 1]
    return new_letter


def get_forth_letter():
    word = words[2]
    if len(word) % 2 == 1:
        old_letter = word[2]
        if old_letter == 'z':
            new_letter = 'a'
        else:
            new_letter = alphabet[alphabet.find(old_letter) + 1]
        print(new_letter)
    else:
        index = round(len(word) / 2) - 1
        old_letter = word[index]
        if old_letter == 'a':
            new_letter = 'z'
        else:
            old_index = alphabet.find(old_letter)
            new_letter = alphabet[old_index - 1]
    return new_letter


def get_fifth_letter():
    count = len(words[0] + words[1]) - 4
    if count > 26:
        count = count % 26
    return alphabet[count - 1]


def get_password():
    return get_first_and_second_letter() + get_third_letter() + get_forth_letter() + get_fifth_letter()


print("Generated password:", get_password())

password = getpass()
result = get_password()
if password == result:
    print("Password is correct")
else:
    print("Password is incorrect!")

