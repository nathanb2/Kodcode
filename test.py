import math

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def calculate_area_of_circle(radius: int) -> float:
    area = 0

    area = math.pi * radius**2

    return area



def reverse_string(text: str) -> str:
    reversed_text = ""

    reversed_text = text[::-1]

    return reversed_text

def is_palindrome(text: str) -> bool:
    is_palindrome = False

    is_palindrome = text == text[::-1]

    return is_palindrome

def sum_of_digits(num: int) -> int:
    sum = 0

    numbers = str(num)
    for number in numbers:
        number = int(number)
        sum += int(number)

    return sum


def find_max(numbers: list) -> float:
    max = 0

    for number in numbers:
        if (number > max):
            max = number

    return max


def km_to_milles(distance_km: float) -> (str, float):
    distance_milles = 0
    error_message = ""

    if(distance_km >= 0):
        distance_milles = distance_km * 1.6
        error_message = ""
    else:
        error_message = "error"

    return error_message, distance_milles


# error, milles = km_to_milles(1)
# print(error, milles)
# print(find_max([3,2,7,89,6,43,22]))
# print(sum_of_digits(345))
# print(is_palindrome("1234321"))
# print(reverse_string("12345"))
# area = calculate_area_of_circle(5)
# print(area)

