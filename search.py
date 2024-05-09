

def lineary_search(numbers: list, to_search: int) -> int:
    to_search_index = -1

    for index, number in enumerate(numbers):
        if number == to_search:
            to_search_index = index
            break

    return to_search_index


def binary_search(numbers: list, to_search: int) -> int:
    to_search_index = -1
    right = len(numbers) - 1
    left = 0

    while (left <= right):
        middle = (left + right) // 2
        if numbers[middle] == to_search:
            to_search_index = middle
            break
        elif numbers[middle] < to_search:
            left = middle + 1
        else:
            right = middle - 1

    return to_search_index


numbers = [1,3,7,9,12,43,67,89]
print(lineary_search(numbers, 99))
print(binary_search(numbers, 99))
