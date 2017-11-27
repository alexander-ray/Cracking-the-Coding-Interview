# Function to calculate number of ways to get to the nth step
# People can take stairs 1, 2, or 3 at a time
# Dynamic programming solution
def possible_steps(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2

    mem = [0 for _ in range(0, n+1)]
    mem[0] = 1
    mem[1] = 1
    mem[2] = 2

    for i in range(3, n+1):
        mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3]

    return mem[n]

def main():
    print(possible_steps(3))

if __name__ == '__main__':
    main()