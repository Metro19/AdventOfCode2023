import enum
from dataclasses import dataclass


class CardOutcomes(enum.Enum):
    FiveOfAKind = 0
    FourOfAKind = 1
    FullHouse = 2
    ThreeOfAKind = 3
    TwoPair = 4
    OnePair = 5
    HighCard = 6


class Cards:
    true_string: str
    corrected_array: list[int]
    corrected_array_sorted: list[int]
    bid: int

    def __init__(self, ts: str, ca: list[int], cas: list[int], bid: int):
        self.true_string = ts
        self.corrected_array = ca
        self.corrected_array_sorted = cas
        self.bid = bid

    def __lt__(self, other):
        self_score = score_hand(self)
        other_score = score_hand(other)

        # greater than
        if self_score.value < other_score.value:
            return True

        # less than
        if self_score.value > other_score.value:
            return False

        # else
        for self_val, other_val in zip(self.corrected_array, other.corrected_array):
            if self_val > other_val:
                return True

            if self_val < other_val:
                return False


def correct_card_array(raw: str) -> list[int]:
    out = []

    for char in raw:
        match char:
            case "T":
                out.append(10)

            case "J":
                out.append(1)

            case "Q":
                out.append(12)

            case "K":
                out.append(13)

            case "A":
                out.append(14)

            case _:
                out.append(int(char))

    return out


def score_hand(hand: Cards) -> CardOutcomes:
    # calculate the number of instances of a number
    instances_of_number = dict()

    for num in hand.corrected_array:
        # check if in instances
        if num in instances_of_number.keys():
            instances_of_number[num] += 1
        else:
            instances_of_number[num] = 1

    # joker correction
    if 1 in instances_of_number.keys() and instances_of_number[1] != 5:
        joker_count = instances_of_number[1]
        del instances_of_number[1]

        # find the highest count
        high_key = -1
        high_amount = -1
        for key in instances_of_number.keys():
            if instances_of_number[key] > high_amount:
                high_amount = instances_of_number[key]
                high_key = key

        # add jokers to highest item
        instances_of_number[high_key] += joker_count


    # five of a kind
    if len(instances_of_number.values()) == 1:
        return CardOutcomes.FiveOfAKind

    # four of a kind
    if 4 in instances_of_number.values():
        return CardOutcomes.FourOfAKind

    # full house
    if len(instances_of_number.values()) == 2:
        return CardOutcomes.FullHouse

    # three of a kind
    if 3 in instances_of_number.values():
        return CardOutcomes.ThreeOfAKind

    # Two pair
    if len(instances_of_number.values()) == 3:
        return CardOutcomes.TwoPair

    # One pair
    if len(instances_of_number.values()) == 4:
        return CardOutcomes.OnePair

    # High Card (default)
    else:
        return CardOutcomes.HighCard


def main():
    # all cards
    all_cards = []
    score = 0

    # read all data
    for line in open("data.txt").read().split("\n"):
        raw_str, bid = line.split(" ")

        corrected_array = correct_card_array(raw_str)

        # load into class
        all_cards.append(Cards(raw_str, corrected_array, sorted(corrected_array), int(bid)))
        # print(line, score_hand(all_cards[-1]))

    result = sorted(all_cards)
    result = reversed(result)

    for loc, val in enumerate(result):
        print(val.true_string)
        score += (loc+1) * val.bid

    print(score)


if __name__ == "__main__":
    main()
