# only valid for depth 2
def encrypt_rail_fence(message, depth=2):
    rails = [[] for _ in range(depth)]

    for i, char in enumerate(message):
        rails[i % depth].append(char)

    cipher_text =''.join(''.join(rail) for rail in rails)
    return cipher_text


def decrypt_rail_fence(message, depth=2):
    rails_length = [len(message) // depth] * depth
    remaining_chars = len(message) % depth
    for i in range(remaining_chars):
        rails_length[i] += 1
    rails = [list(message[i:i + rails_length[j]]) for j, i in enumerate(range(0, len(message), max(rails_length)))]

    msg = ''
    for _ in range(len(message)):
        for i in range(depth):
            if rails[i]:
                msg += rails[i].pop(0)
    return msg


encrypted = encrypt_rail_fence('attackatonce')
print(encrypted)
print(decrypt_rail_fence(encrypted))