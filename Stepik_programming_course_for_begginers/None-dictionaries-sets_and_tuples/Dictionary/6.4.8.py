from string import ascii_lowercase

alphabet = {}
for i in ascii_lowercase:
    alphabet.update({i: ord(i) - 96})
print(alphabet)
