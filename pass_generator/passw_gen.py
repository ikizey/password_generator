import secrets
import string

PASS_LEN = 20
LIST_LEN = 10


def gen_lower():
    passwords = [''.join(secrets.choice(string.ascii_lowercase)
                         for _ in range(PASS_LEN)) for _ in range(LIST_LEN)]
    return passwords


def gen_lower_upper():
    passwords = [''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase)
                         for _ in range(PASS_LEN)) for _ in range(LIST_LEN)]
    return passwords


def gen_num():
    passwords = [''.join(secrets.choice(string.digits)
                         for _ in range(PASS_LEN)) for _ in range(LIST_LEN)]
    return passwords


def gen_char_num():
    passwords = [''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
                         for _ in range(PASS_LEN)) for _ in range(LIST_LEN)]
    return passwords

