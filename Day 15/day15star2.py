import dataclasses


@dataclasses.dataclass
class Lens:
    label: str
    number: int


def hash_score_string(input_string: str) -> int:
    score = 0

    for char in input_string:
        score += ord(char)
        score *= 17
        score = score % 256

    return score


def handle_dash(label: str, binnifer: list[list[Lens]]):
    label = label[0:-1]
    hash_score = hash_score_string(label)

    # check for label
    for loc, item in enumerate(binnifer[hash_score]):
        if item.label == label:
            binnifer[hash_score].pop(loc)


def handle_equals(label: str, binnifer: list[list[Lens]]):
    # setup
    label, foc_len = label.split("=")
    lens_item = Lens(label, int(foc_len))
    hash_score = hash_score_string(label)

    # check for label
    for loc, item in enumerate(binnifer[hash_score]):
        if item.label == label:
            binnifer[hash_score][loc] = lens_item
            return

    # push
    binnifer[hash_score].append(lens_item)


def main():
    # create 2D array
    binnifer: list[list[Lens]] = [[] for _ in range(256)]

    for label in open("data.txt").read().split(","):
        hash_score = hash_score_string(label)

        # dash
        if "-" in label:
            handle_dash(label, binnifer)

        # equals
        if "=" in label:
            handle_equals(label, binnifer)

    # scoring
    score = 0
    for loc1, bin in enumerate(binnifer):
        for loc2, item in enumerate(bin):
            tmp_score = loc1 + 1
            tmp_score *= loc2 + 1
            tmp_score *= item.number
            score += tmp_score

    print(score)



if __name__ == '__main__':
    main()
