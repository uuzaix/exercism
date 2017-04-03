import re

def is_pangram(sentence):
    letters = re.findall("[a-z]", sentence.lower())
    if len(set(letters)) != 26:
        return False
    return True
