# Note: I accidentally used DP on this problem when it was not needed.
# Kinda fun though.


def score_card(winning_numbers: list[int], played_numbers: list[int]) -> int:
    score = 0

    for num in played_numbers:
        if num in winning_numbers:
            score += 1

    return score


def score_one_card(number_to_score: int, next_cards: list[int], DP: list[int]) -> int:
    # check if number has already been calculated
    if DP[number_to_score] != -1:
        return DP[number_to_score]

    # None more to return
    if next_cards[number_to_score] == 0:
        return 1

    # calculate number
    total = 1
    for i in range(number_to_score + 1, next_cards[number_to_score] + number_to_score + 1):
        res = score_one_card(i % len(next_cards), next_cards, DP)
        DP[i % len(next_cards)] = res
        total += res

    DP[number_to_score] = total
    return total


def main():
    score = 0
    next_cards: list[int] = []
    DP: list[int] = []

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
        next_cards.append(score_card(winning_numbers, played_numbers))

    # create blank DP
    DP = [-1 for _ in range(0, len(next_cards))]

    # score everything
    for i in range(len(next_cards)):
        score += score_one_card(i, next_cards, DP)

    print(score)


if __name__ == "__main__":
    main()
