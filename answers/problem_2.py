def main():
    prev_val = 0
    next_val = 1
    sum_val = 0

    while next_val < 4_000_000:
        new_val = prev_val + next_val
        prev_val, next_val = next_val, new_val

        if new_val % 2 == 0:
            sum_val += new_val

    print(f"Answer: {sum_val}")


if __name__ == "__main__":
    main()
