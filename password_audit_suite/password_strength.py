import math
import string

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in string.punctuation for c in password): pool += 32

    return len(password) * math.log2(pool) if pool else 0

def strength_rating(password):
    entropy = calculate_entropy(password)
    if entropy < 28:
        return "Weak"
    elif entropy < 36:
        return "Moderate"
    else:
        return "Strong"
