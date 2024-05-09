

def reverse_string(string: str) -> str:

    if len(string) <= 1:
        return string

    return string[-1] + reverse_string(string[:-1])


def fibonacci(n) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-2) + fibonacci(n-1)


def list_sum(data_list: list)-> int:

    if len(data_list) == 1:
        return data_list[0]

    return data_list[0] + list_sum(data_list[1:])

# print(reverse_string("12345"))
# print(fibonacci(6))
# print(list_sum([2,5,7,8,4]))

def merge(arr1: list, arr2: list) -> list:
    i1 = 0
    i2 = 0
    result = []

    while i1 < len(arr1) and i2 < len(arr2):

        if arr1[i1] < arr2[i2]:
            result.append(arr1[i1])
            i1 += 1
        else:
            result.append(arr2[i2])
            i2 += 1

    result += arr1[i1:]
    result += arr2[i2:]

    return result

def merge_sort(numbers: list) -> list:

    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)

print(merge_sort([2,0,31,32,12]))


def binary_search_recursive(numbers: list, to_search: int, left: int, right: int) -> int:
    result_index = -1

    middle = (right + left) // 2

    if right < left:
        return result_index

    elif to_search == numbers[middle]:
        result_index = middle
    elif to_search > numbers[middle]:
        result_index = binary_search_recursive(numbers, to_search, middle + 1, right)
    else:
        result_index = binary_search_recursive(numbers, to_search, left, middle - 1)

    return result_index


numbers = [2,5,7,9,90]
print(binary_search_recursive(numbers, 9, 0, len(numbers) - 1,))