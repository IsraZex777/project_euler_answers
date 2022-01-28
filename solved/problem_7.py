import math


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


def main():
    value = 3
    counter = 1
    prime_numer = 2

    while counter < 10001:
        if is_prime(value):
            counter += 1
            prime_numer = value

        value += 2

    print(f"10001's prime number is {prime_numer}")


if __name__ == "__main__":
    main()
