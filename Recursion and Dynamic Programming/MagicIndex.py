import math

# Function to find a single index where arr[i] == i or return -1 if it doesn't exist
# arr must be sorted in ascending order
# Binary search variant
def magic_index(arr, mindex, maxdex):
    mid = math.ceil((maxdex+mindex)/2)
    if mindex > maxdex:
        return -1
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return magic_index(arr, mid + 1, maxdex)
    else:
        return magic_index(arr, mindex, mid - 1)

    return -1

def main():
    arr = [0, 2, 3, 4, 5, 6, 7, 8, 9]
    print(magic_index(arr, 0, 8))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(magic_index(arr, 0, 8))

    arr = [1, 2, 3, 4, 4, 6, 7, 8, 9]
    print(magic_index(arr, 0, 8))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 8]
    print(magic_index(arr, 0, 8))


if __name__ == '__main__':
    main()