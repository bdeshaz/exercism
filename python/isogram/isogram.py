def is_isogram(word):

    # make word lowercase
    word = word.lower()
    # remove spaces
    word = word.replace(" ", "")
    # remove hypen, if present
    word = word.replace("-", "")
    # Check if duplicated char
    if len(word) != len(set(word)):
        return False
    # Check if empty string
    elif not word:
        return True

    return True
