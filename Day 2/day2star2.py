def game(line: str) -> bool:
    # break off colors
    left, right = line.split(": ")
    mins = {"red": 0, "blue": 0, "green": 0}

    # separate into individual draw
    for grab in right.split("; "):

        # separate all colors
        for color in grab.split(", "):
            value, color_name = color.split(" ")

            # get max value needed
            mins[color_name] = max(mins[color_name], int(value))

    return mins["red"] * mins["green"] * mins["blue"]


def main():
    score = 0

    # read from file
    for line in open("data.txt").read().split("\n"):
        # process each line
        score += game(line)

    print(score)


if __name__ == "__main__":
    main()
