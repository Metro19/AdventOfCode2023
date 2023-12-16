def hash_score_string(input: str) -> int:
    score = 0

    for char in input:
        score += ord(char)
        score *= 17
        score = score % 256

    return score


def main():
    score = 0
    for string in open("data.txt").read().split(","):
        score += hash_score_string(string)

    print(score)


if __name__ == "__main__":
    main()
