import re

def is_isogram(word):
    letters = re.findall("[a-z]", word.lower())
    if len(set(letters)) < len(letters):
        return False
    return True

