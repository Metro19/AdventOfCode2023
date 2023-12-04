# input
TRUE_VALS = {"red": 12, "blue": 14, "green": 13}


def game(line: str, true_values: dict) -> bool:
    # break off colors
    left, right = line.split(": ")

    # separate into individual draw
    for grab in right.split("; "):

        # separate all colors
        for color in grab.split(", "):
            value, color_name = color.split(" ")

            # check against true value
            if true_values[color_name] < int(value):
                return False

    return True


def main():
    line_count = 1
    score = 0

    # read from file
    for line in open("data.txt").read().split("\n"):
        # check if valid
        if game(line, TRUE_VALS):
            score += line_count

        line_count += 1

    print(score)


if __name__ == "__main__":
    main()
