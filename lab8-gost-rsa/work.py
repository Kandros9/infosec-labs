from random import randint
import sys

from gost_algorithm import gost_encode, gost_decode
from rsa_algorithm import encrypt_string, decrypt_string

message = "resources/message.txt"
enc_file = "resources/encoded_text.txt"
dec_file = "resources/decoded.txt"
key_file = "resources/rsa_key.txt"


# случайный ключ для ГОСТ
gost_key = randint(0, 10000000000000000000000000000000)

# зашифровка message.txt с помощью ГОСТ
gost_encode(message, enc_file, gost_key)

# зашифровка ключа для ГОСТ с помощью RSA и запись в rsa_key.txt
encoded_gost_key = encrypt_string(str(gost_key))
with open(key_file, 'w') as file:
    file.write(' '.join([str(ord(x)) for x in encoded_gost_key]))




