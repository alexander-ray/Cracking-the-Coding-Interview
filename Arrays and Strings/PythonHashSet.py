'''
Python hashset implementation
Used for hashing strings
'''

def lookup():
    return 0

def hash(str, num_buckets):
    ret = 0
    for c in str:
        ret += ord(c)
    return ret % num_buckets

# Tester driver function
def main():
    size = int(input("Number of buckets"))
    table = [set() for x in range(0, int(size))]
    print(table)

    i = ''
    while True:
        i = input("string")
        if (i == '-1'):
            return 0
        table[hash(i, size)].add(i)
        print(table)

if __name__ == '__main__':
    main()