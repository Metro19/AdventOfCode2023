def score_card(winning_numbers: list[int], played_numbers: list[int]) -> int:
    score = 0

    for num in played_numbers:
        if num in winning_numbers:
            # if score is zero, it becomes one
            if score == 0:
                score = 1
            else:
                score *= 2

    return score


def main():
    score = 0

    # break file down line by line
    for line in open("data.txt").read().split("\n"):
        # setup vars
        winning_numbers: list[int] = []
        played_numbers: list[int] = []

        trash, whole_card = line.split(":")

        # split into winners and all numbers
        winners, numbers = whole_card.split("|")

        # put winners into list
        for w in winners.split():
            winning_numbers.append(int(w))

        # put played numbers into list
        for p in numbers.split():
            played_numbers.append(int(p))

        # score card
        score += score_card(winning_numbers, played_numbers)

    print(score)

if __name__ == "__main__":
    main()
