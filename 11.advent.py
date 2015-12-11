from inputs import ELEVENTH

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def base26_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def base26_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


def next_pw(current):
    current_pw = current
    while True:
        current_pw = base26_encode(base26_decode(current_pw) + 1)
        print "{} ?".format(current_pw)
        for forbidden in ['i','o','l']:
            if forbidden in current_pw:
                continue

        double_letter = []
        straight = False
        for letter in ALPHABET:
            if '{}{}'.format(letter,letter) in current_pw:
                double_letter.append(letter)

            if letter in ALPHABET[:-2]:
                if '{}{}{}'.format(
                    letter,
                    base26_encode(base26_decode(letter) + 1),
                    base26_encode(base26_decode(letter) + 2)) in current_pw:
                    straight = True

        if not len(double_letter) > 1:
            continue

        if not straight:
            continue

        return current_pw

pw1 = next_pw(ELEVENTH.input)
print pw1
pw2 = next_pw(pw1)
print pw2

