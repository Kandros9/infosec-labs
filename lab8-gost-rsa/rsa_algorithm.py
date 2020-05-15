p = 89
q = 61

n = p * q
phi = (p-1)*(q-1)


def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x, phi):
            l.remove(x)
    return l


cop = coprimes(phi)
e = cop[0]
d = modinv(e, phi)


def encrypt_block(m):
    c = modinv(m**e, n)
    if not c:
        print('No modular multiplicative inverse for block ' + str(m) + '.')
        return 0
    return c


def decrypt_block(c):
    m = modinv(c**d, n)
    if not m:
        print('No modular multiplicative inverse for block ' + str(c) + '.')
        return 0
    return m


def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])


def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
