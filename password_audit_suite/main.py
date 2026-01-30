from dictionary_generator import generate_dictionary
from brute_force_simulator import brute_force
from password_strength import strength_rating
from hash_utils import hash_password
from report_generator import generate_report

users = {
    "user1": "password123",
    "user2": "admin"
}

hashes = {u: hash_password(p) for u, p in users.items()}

dictionary = generate_dictionary(["password", "admin", "welcome"])

results = {}

for user, hash_val in hashes.items():
    found = None
    for word in dictionary:
        if hash_password(word) == hash_val:
            found = word
            break

    if not found:
        found = brute_force(hash_val)

    results[user] = {
        "password": found,
        "strength": strength_rating(found) if found else "Unknown"
    }

generate_report(results)
