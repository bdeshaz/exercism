from re import sub

def is_pangram(words):
    """
        Thanks to DUznanki for help on solution
        I explored re.sub and regex format due to their solution.
        As well, realized a conditional can be returned
    """

	letters = set(sub('[^a-z]','',words.lower()))
	return len(letters) == 26
