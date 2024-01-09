def main():
    # read in data
    raw_in = open("data.txt").read().split("\n")

    # break into int lists
    formatted_lists = []
    for l in raw_in:
        nl = []
        for i in l.split(" "):
            nl.append(int(i))

        formatted_lists.append(nl)

    score = 0
    for f in formatted_lists:
        score += process_list(f)

    print(score)


def process_list(input_list: list[int]) -> int:
    sub_lists = [input_list]

    while check_all_zeros(sub_lists[-1]):
        sub_lists.append(calculate_new_list(sub_lists[-1]))

    return fill_all_values_left(sub_lists)


def fill_all_values_left(list_of_lists: list[list[int]]) -> int:
    carryover_val = 0
    for l in list_of_lists[::-1]:
        carryover_val = l[0] - carryover_val
        l.append(carryover_val)

    return carryover_val


def calculate_new_list(input_list: list[int]) -> list[int]:
    new_list = []

    for loc in range(0, len(input_list) - 1):
        new_list.append(input_list[loc + 1] - input_list[loc])

    return new_list


def check_all_zeros(input_list: list[int]) -> bool:
    for i in input_list:
        if i != 0:
            return True

    return False


if __name__ == '__main__':
    main()
