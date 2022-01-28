import math
import numpy as np


def is_palindrome(number: int):
    num_str = str(number)

    for index in range(int(len(num_str) / 2)):
        if num_str[index] != num_str[-index - 1]:
            return False

    return True


def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    factor = 3
    num_sqrt = math.sqrt(num)
    while factor <= num_sqrt:
        if num % factor == 0:
            return False

        factor += 2

    return True


def find_next_prime_number(num: int):
    """
    Finds the next prime number

    :param num: Input prime number
    :return:
    """
    if num == 2:
        return 3

    if num % 2 == 0 or num == 1:
        raise IndexError("Input number is not prime")

    num += 2
    while not is_prime(num):
        num += 2

    return num


def find_all_prime_factors(num: int) -> list:
    """
    returns list of all prime factors of the input number

    :param num: Input number
    :return:
    """
    prime_factor = 2
    factors = []

    while num != 1:
        if num % prime_factor == 0:
            num /= prime_factor
            factors.append(prime_factor)
        else:
            prime_factor = find_next_prime_number(prime_factor)

    return factors


def get_factors_of_all_numbers_less_than(num: int) -> dict:
    """
    Creates number to factors dict of all numbers less then 'num'
    :param num:
    :return:
    """
    factor_mat = [[] for index in range(0, num + 1)]

    # adds factors to the proper products
    for curr_factor in range(1, num + 1):
        products = range(curr_factor, num + 1, curr_factor)

        # Adds index into each products' factor list (instead of the index product)
        for product in products[1:]:
            factor_mat[product].append(curr_factor)

    product_to_factors = {}
    # adds factors to the matrix
    for product in range(1, num + 1):
        product_to_factors[product] = factor_mat[product]

    return product_to_factors


# if __name__ == "__main__":
#     get_factors_of_less_than(10000)
