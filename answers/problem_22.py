import numpy as np


def word_to_score(word: str) -> int:
    """
    Converts A-Z  to its numberic sum
    for example ABCN = 1 + 2 + 3 + 14

    :param word: input word
    :return: Score
    """
    score = sum([ord(char) - ord('A') + 1 for char in word])
    return score


def answer_1():
    with open("./data/p022_names.txt") as file:
        names = file.read().replace("\"", "").split(",")
        names.sort()

    text_sum = sum([index * word_to_score(name) for index, name in enumerate(names, 1)])
    return text_sum


if __name__ == "__main__":
    answer = answer_1()
    print(f"Answer: {answer}")
