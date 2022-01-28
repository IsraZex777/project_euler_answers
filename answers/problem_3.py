from utils import is_prime


def answer_1(num):
    factor = 3
    was_found = False
    max_prime_factor = 3

    while not was_found:
        if num % factor == 0:
            num = int(num / factor)

            if is_prime(num):
                max_prime_factor = num
                was_found = True

        factor += 2

    return max_prime_factor


if __name__ == "__main__":
    num = 600851475143
    answer = answer_1(num)
    print(f"Answer: {answer}")
