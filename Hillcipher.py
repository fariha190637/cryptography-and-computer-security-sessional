import numpy as np
import string

alphabet = string.ascii_lowercase
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x


def mat_inv(det, modulus):
    gcd, x, y = egcd(det, modulus)
    if gcd != 1:
        raise Exception('Inverse is not possible')
    else:
        return (x % modulus + modulus) % modulus


def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mat_inv(det, modulus)
    matrix_modulus_inv = (
            det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_modulus_inv


def encrypt_decrypt(message, key):
    msg = ''
    msg_in_numbers = [letter_to_index[char] for char in message]
    split_p = [
        msg_in_numbers[i:i + len(key)]
        for i in range(0, len(msg_in_numbers), len(key))
    ]
    for P in split_p:
        P = np.transpose(np.asarray(P))[:, np.newaxis]
        while len(P) != len(key):
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]
        numbers = np.dot(key, P) % len(alphabet)
        n = len(numbers)
        for idx in range(n):
            number = numbers[idx][0]
            msg += index_to_letter[number]
    return msg


message = "help"
key = ([[3, 3], [2, 5]])
Kinv = matrix_mod_inv(key, len(alphabet))
encrypted_message = encrypt_decrypt(message, key)
print(encrypted_message.upper())
decrypted_message = encrypt_decrypt(encrypted_message, Kinv)
print(decrypted_message.upper())