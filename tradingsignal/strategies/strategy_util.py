from typing import List


def cross_over(input_data: List, value: int):
    """return true if input_data crossed over value otherwise false"""
    return input_data[-1] > value > input_data[-2]


def cross_under(input_data: List, value: int):
    """return true if input_data crossed under value otherwise false"""
    return input_data[-1] < value < input_data[-2]
