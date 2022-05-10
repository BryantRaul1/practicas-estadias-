import string
import secrets


def get_random_string(size):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(letters) for i in range(size))


def get_random_email():
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(letters) for i in range(12)) + 'z.ttgfqh9d@mailosaur.io'
