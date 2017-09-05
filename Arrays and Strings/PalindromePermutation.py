#!/usr/local/bin/python3.6

def is_palindrome(str):
    size = len(str)
    if (size % 2 == 0):
        front = str[0:size/2]
        back = str[size/2:]
        if (front == back[::-1]):
            return True
        else:
            return False
    else:
        front = str[0:size/2]
        back = str[size/2 + 1:]
        if (front == back[::-1]):
            return True
        else:
            return False

def perm_palindromes(a, l, r):
    if (l == r):
        if (is_palindrome(toString(a))):
            print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            perm_palindromes(a, l+1, r)
            a[l], a[i] = a[i], a[l]

def main():
    str = "tact coa"
    perm_palindromes(str, 0, len(str))

if __name__ == '__main__':
    main()
