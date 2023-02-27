from string import punctuation
import string


def longest_word_in_file(file_name):
    simbol = []
    file = open(file_name, 'r+', encoding='utf-8')
    f = file.read()
    for i in f:
        if i in string.punctuation:
            f = f.replace(i, ' ')
        if i == "\n":
            f = f.replace(i, ' ')
    for i in f.split(' '):
        simbol.append(i)
        if len(simbol) > 1:
            if len(i) == len(simbol[0]):
                simbol.pop(0)
            if len(simbol) > 1:
                if len(simbol[0]) > len(i):
                    simbol.pop(1)
                if len(simbol) > 1:
                    if len(i) > len(simbol[0]):
                        simbol.pop(0)
    if len(simbol) == 1:
        return simbol[0]
    elif len(simbol) == 2:
        return simbol[1]
