import random


def get_fibonachi(max_limit: int) -> list:

    if(max_limit == 0):
        return [0]

    fibonachi_suite = [0,1]

    while fibonachi_suite[-1] + fibonachi_suite[-2] <= max_limit:

        fibonachi_new_item = fibonachi_suite[-1] + fibonachi_suite[-2]
        fibonachi_suite.append(fibonachi_new_item)

    return fibonachi_suite


# print(get_fibonachi(1000))


def get_prime_numbers(max_limit: int) -> list:
    prime_numbers = []

    #find prime numbers

    for number in range(2, max_limit + 1):
        is_prime = True
        for divider in range(2, number):
            if number % divider == 0:
                is_prime = False
                break
        if(is_prime):
            prime_numbers.append(number)

    return prime_numbers


# print(get_prime_numbers(20))



def get_special_multipliation(list_len: int)-> list:
    base_list = []
    special_multi_list = []

    for i in range(list_len):
        base_list.append(random.randint(1,10))
    print(base_list)

    count = 1

    base_list = base_list[::-1]
    print(base_list)

    while len(base_list) - count >= 0:

        new_item = 1
        for i in range(count):
            new_item *= base_list.pop()

        count += 1
        special_multi_list.append(new_item)

    return special_multi_list

# print(get_special_multipliation(10))


# (1) + (2 x 3) + (4 x 5 x 6) + (7 x 8 x 9 x 10)
def get_special_multiplication_sum(limit: int) -> int:
    sum = 0
    multiples_sum = 1
    multiplication_quantity = 1
    multiplication_counter = 0


    for number in range(1, limit + 1):

        multiples_sum *= number

        multiplication_counter += 1

        if(multiplication_counter == multiplication_quantity):

            sum += multiples_sum
            multiples_sum = 1
            multiplication_quantity += 1
            multiplication_counter = 0


    return sum


# print(get_special_multiplication_sum(10))


def get_special_multiplication_sum(limit):
    sum_result = 0
    multiple_sum = 1
    multiple_quantity = 1
    counter = 0

    for number in range(1, limit + 1):
        multiple_sum *= number
        counter += 1

        if counter == multiple_quantity:
            sum_result += multiple_sum
            counter = 0
            multiple_quantity += 1
            multiple_sum = 1

    return sum_result

# Example usage:
# result = get_special_multiplication_sum(5)
# print("Result:", result)


def find_max_in_nested_list(nested_list: list) -> int:
    max = 0

    for list in nested_list:
        for number in list:
            if number > max:
                max = number

    return max



# numbers = [[1, 3, 5], [9, 2, 4, 8], [7, 6]]
# print(find_max_in_nested_list(numbers))


def fill_sets(data: dict, values: list) -> dict:
    set_number = 1
    for value in values:
        if(len(data['set' + str(set_number)]) < 3):
            (data['set' + str(set_number)]).add(value)
            if len(data['set' + str(set_number)]) == 3:
                set_number += 1
        else:
            set_number += 1
    print(data)
    return data

data = {
    'set1': set(),
    'set2': set(),
    'set3': set()
}
values = [10, 20, 20, 5, 30, 15, 25, 35, 5]
fill_sets(data, values)
print(find_max_value_in_dict_set(data))

