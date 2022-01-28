import numpy as np


def main():
    max_value = 1000
    factors = np.array([3, 5])

    result = np.sum([value for value in range(max_value) if
                     ((value % factors) == 0).any()])

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
