#!/usr/bin/env python
import collections
import itertools
import sys




def get_all_combinations(letters, center_letter):
    combinations = []
    for n in range(3, 7):
        combinations.extend([''.join(sorted(list(ls)+[center_letter])) for ls in itertools.combinations(letters, n)])
    return combinations

    
def solve_puzzle(center_letter, other_letters):
    dd = load_words()
    found_words = []
    for word in get_all_combinations(other_letters, center_letter):
        if word in dd:
            found_words.extend(dd[word])
    words = sorted(list(set(found_words)))
    print(f"Found {len(words)} words!")    
    return sort_into_length(words)

def sort_into_length(words):
    d = collections.defaultdict(list)
    for word in words:
        d[len(word)].append(word)
    out = []
    for length in sorted(d.keys()):
        out.extend(d[length])
    return out

def load_words():

    lines = open('words.txt').readlines()
    words = [l.strip() for l in lines]
    dd = collections.defaultdict(list)
    for w in words:
        if w[0].isupper():
            continue
        key = ''.join(sorted(set(w)))
        dd[key].append(w.lower())

    return dd


def print_in_columns(l, ncols):

    # split into three
    def chunk(l, n):
        for ix in range(0, len(l), n):
            yield l[ix:ix+n]

    nrows = len(l) // ncols
    if len(l) % ncols > 0:
        nrows += 1

    cols = [_ for _ in chunk(l, nrows)]

    nrows = max([len(col) for col in cols])

    for w1, w2, w3 in itertools.zip_longest(*cols):
        if w1 is None: 
            w1 = ''
        if w2 is None: 
            w2 = ''
        if w3 is None: 
            w3 = ''
        print(f'{w1:10} {w2:10} {w3:10}')


def main():

    letters = sys.argv[1]

    if len(letters) == 7:
        pass
    else:
        letters = input("Input letters starting with center letter and then the rest in any order: ")
        letters = letters.strip()

    if len(letters) != 7:
        raise ValueError("You must type in 7 letters!")

    answers = solve_puzzle(letters[0], letters[1:])

    print_in_columns(answers, 3)

if __name__ == "__main__":
    main()
