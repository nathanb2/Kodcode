

def calculations(first_number: int, second_number: int) -> list:

    return [add(first_number, second_number), substract(first_number, second_number)]


def substract(first_number, second_number):
    return first_number - second_number


def add(first_number, second_number):
    return first_number + second_number


def multi_sum(*args) -> int:
    result: int = 0
    for arg in args:
        result += arg
    return result



print(calculations(2, 4))
print(multi_sum(2, 4))