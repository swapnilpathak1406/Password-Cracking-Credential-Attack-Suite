import itertools
import string
from hash_utils import hash_password


def brute_force(hash_value, algo="sha256", max_length=4):
    characters = string.ascii_lowercase + string.digits

    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            guess = ''.join(attempt)
            if hash_password(guess, algo) == hash_value:
                return guess

    return None
