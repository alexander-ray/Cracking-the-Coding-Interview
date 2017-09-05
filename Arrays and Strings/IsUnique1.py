#!/usr/local/bin/python3.6

# No auxilary data structure
# Theta(n^2)
# n * ((n - 1) + (n - 2) + ... + 1)
def is_unique_dumb(str):
    for i in range (0, len(str)):
        for j in range (i + 1, len(str)):
            if (str[i] == str[j]):
                return False
    return True

def is_unique(str):
    # Assume in ascii char set
    if (len(str) > 128):
        return False
    else:
        char_set = [False for _ in range(0, 128)]
        for i in range(0, len(str)):
            if (char_set[ord(str[i])] == True):
                return False
            else:
                char_set[ord(str[i])] = True
        return True

def main():
    test = "test string"
    test2 = "zxcvbnmas qwerty"
    print(is_unique(test))
    print(is_unique(test2))

if __name__ == '__main__':
    main()
