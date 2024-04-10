from datetime import datetime
import random


def find_min_index(numbers: list) -> int:
    min_index = 0

    for index in range(len(numbers)):
        if numbers[index] < numbers[min_index]:
            min_index = index

    return min_index


def selection_sort(numbers: list) -> list:
    list_length = len(numbers)

    for index in range(list_length):

        min_index = index + find_min_index(numbers[index:])
        numbers[index], numbers[min_index] = numbers[min_index], numbers[index]

    return numbers


def bubble_sort(numbers: list) -> list:
    list_length = len(numbers)
    bubble_counter = 0

    for i in range(list_length - 1):
        sorted = True
        for index in range(list_length - 1 - i):# [2,5,7,9,3]
            if(numbers[index] > numbers[index + 1]):
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                sorted = False

        if sorted:
            break

    return numbers


list = random.sample(range(0, 1000), 20)
print(selection_sort(list))
print(bubble_sort(list))
