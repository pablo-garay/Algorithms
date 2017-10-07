from collections import Counter

def number_needed(a, b):
    ht = Counter()
    chars_to_delete = 0

    for letter in a:
        ht[letter] += 1

    for letter in b:
        ht[letter] -= 1

    for char in ht:
        if ht[char] != 0:
            chars_to_delete += abs(ht[char])

    return chars_to_delete


a, b = ("cde", "abc")
print number_needed(a, b)

