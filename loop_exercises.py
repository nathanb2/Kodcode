# ex 1
def custom_print(m_list: list) -> None:
    for number in m_list:
        if number > 10:
            print(number - 10)
        else:
            print(number)


list1 = [1, 4, 677, 3, 2, 43]


# custom_print(list1)


# ex2
def custom_factorial_sum(max: int) -> int:
    sum = 0

    for number in range(1, max + 1):
        sum += number ** 2

    return sum


# n_str = input("please insert number")
# n = int(n_str)
#
# print(custom_factorial_sum(n))

# ex3


def count_dividable_digits(number: int, divider: int) -> int:
    dividable_digits_count = 0

    while number > 0:
        unit = number % 10
        if unit != 0 and unit % divider == 0:
            dividable_digits_count += 1
        number = number // 10

    return dividable_digits_count


# print(count_dividable_digits(1234567890, 2))


# ex4

# input of numbers
# loop : while (input >= 0)

def find_input_infos():
    inputted_number = 0
    max_num = 0
    min_num = 0
    count_even_num = 0
    count_odd_num = 0
    sum = 0
    count = 0
    average = 0

    inputted_number = int(input("Please enter a positive number"))

    if inputted_number == -1:
        print("try again")

    while (inputted_number >= 0):

        count += 1

        if inputted_number > max_num:
            max_num = inputted_number

        if inputted_number < min_num or sum == 0:
            min_num = inputted_number

        sum += inputted_number

        if inputted_number % 2 == 0:
            count_even_num += 1
        else:
            count_odd_num += 1

        inputted_number = int(input("Please enter a positive number"))

    average = sum / count

    print("max_num", max_num)
    print("min_num", min_num)
    print("count", count)
    print("count_even_num", count_even_num)
    print("count_odd_num", count_odd_num)
    print("sum", sum)
    print("average", average)


# find_input_infos()

def is_palindrome(number: int) -> bool:
    is_palindrome = False

    temp = number
    digit_count = 0

    while temp > 0:
        digit_count += 1
        temp //= 10

    temp = number
    right_half = 0
    left_half = number

    for index in range(digit_count // 2):
        right_half *= 10
        right_half += temp % 10
        temp //= 10

        left_half //= 10

    if digit_count % 2 == 1:
        left_half //= 10

    is_palindrome = right_half == left_half

    return is_palindrome


print(is_palindrome(12321))
print(is_palindrome(1221))
print(is_palindrome(1321))
print(is_palindrome(1329))


def sub_list_by_char(text: str, last_char: str):
    sub_text = ""
    for char in text:
        sub_text += char
        if char == last_char:
            break
    print(sub_text)

sub_list_by_char("natjskc", "j")