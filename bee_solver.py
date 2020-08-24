#!/usr/bin/env python
import collections
import itertools
import sys




def get_all_combinations(letters, center_letter):
    """
    Get all combinations of unique letters that include the center_letter for
    unique sets of length 4 and up
    """
    combinations = []
    for n in range(1, 7):
        combinations.extend([''.join(sorted(list(ls)+[center_letter])) for ls in itertools.combinations(letters, n)])
    return combinations

def sort_into_length(words):
    """Sort all the words into length order.  They will already in sorted
    alphabetically"""
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


def min_length(words, min_length=4):
    """Filter out all words less than the minimum length"""
    return [word for word in words if len(word) >= min_length]


    
def solve_puzzle(center_letter, other_letters):
    """Solve the puzzle"""
    word_dict = load_words()
    found_words = []
    for word in get_all_combinations(other_letters, center_letter):
        if word in word_dict:
            found_words.extend(word_dict[word])
    words = sorted(list(set(found_words)))
    print(f"Found {len(words)} words!")    
    return sort_into_length(min_length(words))


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
