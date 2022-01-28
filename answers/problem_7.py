from utils import is_prime


def main():
    value = 3
    counter = 1
    prime_number = 2

    while counter < 10001:
        if is_prime(value):
            counter += 1
            prime_number = value

        value += 2

    print(f"10001's prime number is {prime_number}")


if __name__ == "__main__":
    main()
