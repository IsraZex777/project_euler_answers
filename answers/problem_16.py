def answer_1():
    product = 2 ** 1000
    result = sum([int(digit) for digit in str(product)])
    return result


if __name__ == "__main__":
    answer = answer_1()
    print(f"Answer: {answer}")
