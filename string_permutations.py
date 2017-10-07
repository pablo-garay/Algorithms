from generate_permutations import *
# from itertools import permutations


def string_permutations(input_string):
    counter = 1

    for permutation in permutations(range(len(input_string))):
        print "%d]" %counter,

        for i in permutation:
            print input_string[i],
        print

        counter += 1

string_permutations(input_string="Pablo")
string_permutations(input_string="123")
