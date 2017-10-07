from collections import Counter

def ransom_note(magazine, ransom):
    dictio = Counter(magazine)

    for word in ransom:
        if word not in dictio:
            return False
        else:
            dictio[word] -= 1
            if dictio[word] < 0:
                return False

    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")
