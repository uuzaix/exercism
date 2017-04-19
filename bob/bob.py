import re


def hey(words):
    text = words.strip()
    if text.isupper():
        return 'Whoa, chill out!'
    elif text.endswith("?"):
        return 'Sure.'
    elif re.findall('\w+', words) == []:
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
