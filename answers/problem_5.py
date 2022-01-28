import math

from utils import find_all_prime_factors


def answer_1():
    prime_to_max_amount = {}

    for num in range(2, 21):
        prime_to_amount = {}
        for prime_factor in find_all_prime_factors(num):
            if prime_factor not in prime_to_amount:
                prime_to_amount[prime_factor] = 0
            prime_to_amount[prime_factor] += 1

        for prime, amount in prime_to_amount.items():
            if prime not in prime_to_max_amount or \
                    prime_to_max_amount[prime] < amount:
                prime_to_max_amount[prime] = amount

    # The answer equals to the product of all the prime factors found
    answer = 1
    for prime, amount in prime_to_max_amount.items():
        answer *= math.pow(prime, amount)

    return int(answer)


if __name__ == "__main__":
    problem_answer = answer_1()
    print(f"Answer: {problem_answer}")
