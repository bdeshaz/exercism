def is_pangram(words):
    words = words.lower().replace(" ", "")
    words = list(set(words))

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    alphabet = list(alphabet)

    print(alphabet)

    for letter in words:
        if letter in alphabet:
            alphabet.remove(letter)

    if len(alphabet) > 0:
        return False

    return True
