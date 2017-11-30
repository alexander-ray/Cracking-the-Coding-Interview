
def num_combinations(denoms, num_cents):
    l = len(denoms)
    # Num_cents + 1 to include 0 cent case
    mem_table = [[0 for _ in range(0, l)] for _ in range(0, num_cents + 1)]
    # For 0 cent case, there exists only one option
    mem_table[0] = [1 for _ in range(0, l)]

    # Loop through number of cents, not including 0th row
    for i in range(1, num_cents + 1):
        for j in range(0, l):
            curr_denom = denoms[j]
            # If possible, add solution without curr_denom
            if i - curr_denom >= 0:
                mem_table[i][j] += mem_table[i - curr_denom][j]
            # If possible, add solution from previous denom
            if j >= 1:
                mem_table[i][j] += mem_table[i][j-1]

    return mem_table[i][l - 1]


def main():
    denom_vals = [1, 5, 10, 25]
    num_cents = 100
    print(num_combinations(denom_vals, num_cents))

    arr = [1, 2, 3]
    n = 4
    print(num_combinations(arr, n))

if __name__ == '__main__':
    main()