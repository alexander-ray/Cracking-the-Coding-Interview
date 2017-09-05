#!/usr/local/bin/python3.6
from collections import Counter

def is_permutation(str1, str2):
    if (len(str1) != len(str2)):
        return False

    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        # Number of items don't match
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True

def main():
    t1 = "asdfghjkl"
    t2 = "lkjhsdgfa"
    t3 = "asdfg"
    print(is_permutation(t1, t2))
    print(is_permutation(t1, t3))

if __name__ == '__main__':
    main()
