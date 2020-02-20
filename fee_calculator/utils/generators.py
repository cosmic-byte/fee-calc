from random import choice
import string


def generate_random_alphanumeric_key(length=10):
    return "".join(choice(string.ascii_letters + string.digits) for _ in range(length))
