import math


def answer_1():
    fact = math.factorial(100)
    digit_sum = sum([int(d) for d in str(fact)])

    return digit_sum


if __name__ == "__main__":
    answer = answer_1()
    print(f"Answer: {answer}")
