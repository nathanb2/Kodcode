



#QUESTION 1

# input [[],[]] output [max of each list]

#[3,6,2] -> 6
def get_max(numbers: list)-> int:
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    return max

# input [[],[]]
def print_max_array(arrays: list)-> None:
    maxes = []

    for array in arrays:
        maxes.append(get_max(array))

    print("max values", maxes)


def generate_array(n: int)-> list:
    array = []

    for i in range(n):
        number = int(input("insert number"))
        array.append(number)

    return array

def main(number_of_arrays: int, item_count_in_arrays: int):
    input_arrays = []
    for i in range(number_of_arrays):
        input_arrays.append(generate_array(item_count_in_arrays))

    print_max_array(input_arrays)

# main(2, 3)


#QUESTION 2

#1: O(n**2) -> n + 3n**2
#2: O(n) -> 2 + 2n
#3: O(2**n) -> 2**(n - 1) + 1
#4: O(1) -> 6
#5: O(log2(n)) -> 5log(n-1) + 1
#6 O(n*log2(n)) -> n * (5log(n-1) + 1) + 2

#QUESTION 3

# [5,4,2,1,-1] -> if is decreasing

#A
def is_reverse_sort(numbers: list) -> bool:
    for index in range(len(numbers) - 1):
        if numbers[index] < numbers[index + 1]:
            return False
    return True

# [9,7,3,2,-3] : 2
def binary_search(numbers: list, to_find: int)-> int:
    to_find_index = -1
    left = 0
    right = len(numbers)-1

    while left <= right:
        middle = (right + left) // 2
        if numbers[middle] == to_find:
            to_find_index = middle
            break
        elif numbers[middle] > to_find:
            left = middle + 1
        else:
            right = middle - 1

    return to_find_index

# [2,5,3,6,3,56,7,7,8,8] : 7
def linear_search(numbers: list, to_find: int)-> int:
    to_find_index = -1

    for index, number in enumerate(numbers):
        if number == to_find:
            to_find_index = index
            break

    return to_find_index



def flexible_search(numbers: list, to_find: int)-> int:

    to_find_index = -1
    sorted = is_reverse_sort(numbers)

    if sorted:
        to_find_index = binary_search(numbers, to_find)
    else:
        to_find_index = linear_search(numbers, to_find)

    return to_find_index


print(flexible_search([5,10,1,-4], -3))


#QUESTION 4
#B
def multiple_digits_rec(number: int)-> int:
    if number < 10:
        return number
    return number % 10 * multiple_digits_rec(number//10)

#A [2,6,3,5,9,2,4]
def optimized_sort(numbers: list)-> list:
    for index in range(len(numbers) -1):
        sorted = True
        for to_compare in range(len(numbers) - index - 1):
            if numbers[to_compare] > numbers[to_compare + 1]:
                numbers[to_compare], numbers[to_compare + 1] = numbers[to_compare + 1], numbers[to_compare]
                sorted = False
        if sorted:
            break
    return numbers

#QUESTION 5

#A
def sort_2_numbers(numbers: list)-> list:

    if numbers[0] > numbers[1]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers

def split_and_sort(numbers: list) -> tuple:

    if len(numbers) <= 2:
        return sort_2_numbers(numbers)

    middle = len(numbers) // 2
    left = split_and_sort(numbers[:middle])
    right = split_and_sort(numbers[middle:])

    return left, right

print(split_and_sort([2,5,8,4,2,6,8,9]))

#B
#a: YES:  because the number of actions to perform doesn't depend on the input length
#b n * log2(n - 1)