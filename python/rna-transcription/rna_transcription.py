def to_rna(sequence):

    output = ""

    rna_letters = list("GCTAU")

    for letter in sequence:
        if letter not in rna_letters or sequence == "U":
            return output
