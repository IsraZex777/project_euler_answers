import numpy as np
from utils import get_factors_of_all_numbers_less_than


def answer_1(num: int) -> int:
    product_to_factors = get_factors_of_all_numbers_less_than(num)
    product_to_factor_sum = {product: sum(factors) for product, factors in product_to_factors.items()}

    # looks for amicable pairs
    amicable_pairs = set()
    for number, score in product_to_factor_sum.items():
        if number != score and \
                score in product_to_factor_sum and \
                product_to_factor_sum[score] == number:
            min_number = min(number, score)
            max_number = max(number, score)
            amicable_pairs.add((min_number, max_number))

    amicable_pairs_sum = 0
    for pair in amicable_pairs:
        amicable_pairs_sum += sum(pair)

    return amicable_pairs_sum


if __name__ == "__main__":
    num = 10000
    answer = answer_1(num)
    print(f"Answer: {answer}")
