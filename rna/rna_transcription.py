def to_rna(dna):
    rna = []
    for el in dna:
        if el == "G":
            rna.append("C")
        elif el == "C":
            rna.append("G")
        elif el == "T":
            rna.append("A")
        elif el == "A":
            rna.append("U")
        else:
            return ""
    return "".join(rna)

