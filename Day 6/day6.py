# insert data in the format of {time: record distance}
DATA = {0: 0}


def one_record(race_duration: int, record_distance: int):
    score = 0

    for curr_duration in range(1, race_duration):
        speed = (race_duration - curr_duration)
        distance = speed * curr_duration

        if distance > record_distance:
            score += 1

    return score


def main():
    total_score = 1

    for k in DATA.keys():
        total_score *= one_record(k, DATA[k])

    print(total_score)


if __name__ == "__main__":
    main()
