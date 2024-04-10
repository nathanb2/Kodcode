

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
