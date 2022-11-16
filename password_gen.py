import random


def generate_pass(num_char=20, chars=True, upper_chars=True, spec_chars=True):
    acceptable_chars = [i for i in range(48, 58)]  # nums
    if chars:
        acceptable_chars += [i for i in range(97, 123)]  # lowercase letters
    if upper_chars:
        acceptable_chars += [i for i in range(65, 91)]  # uppercase letter
    if spec_chars:
        acceptable_chars += [i for i in range(34, 44)] \
                            + [i for i in range(45, 48)] \
                            + [i for i in range(58, 65)] \
                            + [i for i in range(91, 97)] \
                            + [i for i in range(123, 127)]  # special characters

    password = ''.join(chr(int(random.choice(acceptable_chars))) for i in range(num_char))
    print('''Your password is >>>''', password)

    return password


def gen_pass_record():
    name = input('''How to name it?\n>> ''')
    login = input('''And what login?\n>> ''')

    return name, login

