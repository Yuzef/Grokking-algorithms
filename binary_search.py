def binary_search(list, item): # return index of the searched item in the list
    low = 0                    # search boundaries
    high = len(list) - 1

    while low <= high:
        mid = low + high
        guess = list[mid]
        if guess == item:      # item found
            return mid
        if guess > item:       # too much
            high = mid - 1
        else:                  # too small
            low = mid + 1

    return None                # item doesn't exist in the list

my_list = [1, 3, 4, 8, 11, 15, 27, 37]

print(binary_search(my_list, 8))
print(binary_search(my_list, 37))
