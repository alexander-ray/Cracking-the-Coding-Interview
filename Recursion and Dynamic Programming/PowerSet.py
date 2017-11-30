# Function to produce a generator of all subsets of a given set s
# Also known as "power set"
def power_set(s):
    n = len(s)

    # precalculating masks
    # powers of two
    masks = [1 << i for i in range(n)]

    # There will be 2^n elements in a powerset for a set of length n
    for i in range(1 << n):
        # Yield is good for instances where one wants to iterate over a result,
        # But all values don't need to be in memory at once
        yield [e for e, mask in zip(s, masks) if i & mask]

def main():
    l = [1, 2, 3, 4]
    g = power_set(l)
    for e in g:
        print(e)

if __name__ == '__main__':
    main()