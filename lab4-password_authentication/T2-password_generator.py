import random
import string
import itertools
import time

symbols = string.ascii_lowercase + string.digits
L = 5
print("A =", len(symbols))
print("L =", L)


def generate_password():
    return ''.join(random.choice(symbols) for i in range(L))


def get_password_time(pswd):
    start_time = time.time()
    for i in itertools.product(symbols, repeat=5):
        result = ''.join(i)
        if pswd == result:
            end_time = time.time()
            print('Time of cracking password:', round(end_time - start_time, 2), " sec")
            break


password = generate_password()
print("Generated password 1:", password)
get_password_time(password)
print()
password = generate_password()
print("Generated password 2:", password)
get_password_time(password)
print()
password = generate_password()
print("Generated password 3:", password)
get_password_time(password)
print()
password = generate_password()
print("Generated password 4:", password)
get_password_time(password)
print()
password = generate_password()
print("Generated password 5:", password)
get_password_time(password)
print()
