from collections import defaultdict

words = ["azizco", "azico", "zizoca"]

encoded = defaultdict(list)

for word in words:
    encoding = [0] * 26
    for letter in word:
        encoding[ord(letter) - ord("a")] += 1
    encoded[tuple(encoding)].append(word)

# print encoded
for num_group, group in enumerate(encoded.values()):
    print num_group, group
