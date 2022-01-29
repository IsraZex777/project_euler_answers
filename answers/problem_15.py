import math

if __name__ == "__main__":
    # convert each vertical vector to "0" and each horizontal to "1".
    # where are 20 "1" vectors, and 20 "0" vectors.
    # We should get all the possible combinations of 20 "0" and 20 "1"
    # This number of combinations equals to the possible ways to get 20 "1"s out of 40
    answer = math.comb(40, 20)
    print(f"Answer: {answer}")
