def generate_dictionary(base_words, max_digits=2):
    wordlist = set()

    for word in base_words:
        wordlist.add(word)
        wordlist.add(word.lower())
        wordlist.add(word.upper())
        wordlist.add(word.capitalize())

        for i in range(10 ** max_digits):
            wordlist.add(f"{word}{i}")

        wordlist.add(word.replace('a', '@').replace('e', '3'))

    return list(wordlist)
