import random
import string

symbols = string.ascii_lowercase + string.digits
L = 5
print("A =", len(symbols))
print("L =", L)


def generate_password():
    return ''.join(random.choice(symbols) for i in range(L))


for i in range(5):
    print("Generated password %s:" % i, generate_password())
