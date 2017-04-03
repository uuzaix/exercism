import re

def word_count(text):
    words = re.findall('[a-z0-9]+', text.lower())
    w_dict = {}
    for word in words:
        if word in w_dict.keys():
            w_dict[word] += 1
        else:
            w_dict[word] = 1
    return w_dict
