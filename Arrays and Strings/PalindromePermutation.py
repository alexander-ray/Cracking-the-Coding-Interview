#!/usr/local/bin/python3.6
from collections import Counter
# Palindrome permutation checker
# Assumes a-z


def toggle(bit_vect, idx):
    if idx < 0:
        return bit_vect
    # Set bitmask
    mask = 1 << idx
    # If idx in bit_vect == 0, set to 1
    if bit_vect & mask == 0:
        bit_vect |= mask
    # Else, set to 0
    else:
        bit_vect &= ~mask
    return bit_vect

# Uses bitvector to keep a running even-odd counter
def bitvector_perm_checker(s):
    s = s.replace(" ", "")
    bit_vect = 0
    for c in s:
        # Find idx, toggle bit
        x = ord(c) - ord('a')
        bit_vect = toggle(bit_vect, x)

    if len(s) % 2 == 0:
        return bit_vect == 0
    elif len(s) % 2 != 0:
        return bit_vect & (bit_vect - 1) == 0
    else:
        return False


def pythonic_perm_checker(s):
    # Necessary to know length of string
    s = s.replace(" ", "")
    count_arr = Counter(s)
    num_odd = 0
    for key in count_arr:
        if not count_arr[key] % 2 == 0:
            num_odd += 1

    if len(s) % 2 == 0 and num_odd == 0:
        return True
    elif len(s) % 2 != 0 and num_odd <= 1:
        return True
    else:
        return False


def main():
    s = "tact coa"
    print(pythonic_perm_checker(s))
    print(bitvector_perm_checker(s))


if __name__ == '__main__':
    main()
