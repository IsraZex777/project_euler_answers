from utils import is_palindrome


def main():
    max_poli = 0
    saved_arg_1 = 0,
    saved_arg_2 = 0,

    for arg_1 in range(999, 100, -1):
        for arg_2 in range(999, 100, -1):
            product = arg_1 * arg_2

            if product < max_poli:
                continue

            if is_palindrome(product):
                max_poli = product
                saved_arg_1 = arg_1
                saved_arg_2 = arg_2

    print(f"best polindrome product is: {max_poli} ({saved_arg_1} * {saved_arg_2})")


if __name__ == "__main__":
    main()
