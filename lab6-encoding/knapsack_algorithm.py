from itertools import combinations
from pathlib import Path

private_key = [2, 3, 6, 13, 27, 52, 105, 210]
m = 420  # должно быть больше суммы всех чисел последовательности
n = 31  # должен быть взаимно простым числом с модулем m
n_inverted = 271  # обратное число по модулю m


def get_public_key():
    public_key = []
    for k in private_key:
        public_key.append((k * n) % m)
    return public_key


public_key = get_public_key()


def convert_to_binary(text):
    s_bin = ''
    for d in text:
        c = str.zfill(bin(ord(d)).replace("0b", ''), 8)
        s_bin += c
    return s_bin


def convert_to_string(bin_text):
    str_data = ''
    for i in range(0, len(bin_text), 8):
        temp_data = bin_text[i:i + 8]
        decimal_data = int(temp_data, 2)
        str_data = str_data + chr(decimal_data)
    return str_data


def encode_message(bin_text):
    result = []
    index = 0
    sum_knapsack = 0
    for bit in bin_text:
        sum_knapsack += int(bit) * public_key[index]
        index += 1
        if index == 8:
            index = 0
            result.append(sum_knapsack)
            sum_knapsack = 0

    return result


def decode_message(message):
    result = ''
    for knapsack in message:
        decoded_knapsack = (int(knapsack) * n_inverted) % m
        for i in range(len(private_key)):
            for var in combinations(private_key, i):
                if sum(var) == decoded_knapsack:
                    s = '0' * len(private_key)
                    for j in var:
                        if j in private_key:
                            p_index = private_key.index(j)
                            s = s[:p_index] + '1' + s[p_index + 1:]
                    result += s
    return result


def send_message(text):
    bin_data = convert_to_binary(text)
    message = encode_message(bin_data)
    return message


def receive_message(message):
    decoded_message = decode_message(message)
    str_text = convert_to_string(decoded_message)
    return str_text


text = Path('resources/message.txt').read_text()

sended = send_message(text)
with open('resources/encoded.txt', 'w') as file:
    file.write(','.join([str(elem) for elem in sended]))

with open('resources/decoded.txt', 'w') as file:
    text = Path('resources/encoded.txt').read_text()
    file.write(receive_message(text.split(',')))


