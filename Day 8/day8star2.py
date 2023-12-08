import math

START_NODE = "AAA"
END_NODE = "ZZZ"
START_LETTER = "A"
END_LETTER = "Z"


def process_node(starts: list[str], nodes: dict, raw: str):
    # split
    start_node, end_nodes = raw.split(" = ")

    # check for A node
    if start_node[-1] == START_LETTER:
        starts.append(start_node)

    # formatting
    l_raw, r_raw = end_nodes.split(", ")
    l_raw = l_raw.replace("(", "")
    r_raw = r_raw.replace(")", "")

    # put into nodes
    nodes[start_node] = [l_raw, r_raw]


def is_list_passing(curr_node_locs: list[str]):
    for node in curr_node_locs:
        if node[-1] != END_LETTER:
            return False

    return True


def get_first_appear(start_node: str, instructions: list[str], nodes: dict) -> int:
    score = 0

    # check all instructions
    while True:
        for i in instructions:
            score += 1
            node_list = nodes[start_node]

            # move nodes
            if i == "L":
                start_node = node_list[0]
            else:
                start_node = node_list[1]

            # quit if end
            if start_node[-1] == END_LETTER:
                return score


def main():
    # vars
    start_nodes = []
    instructions: list[str]
    score_start_nodes = []
    nodes = dict()
    score = 0

    # pull data from file
    letters, nodes_raw = open("data.txt").read().split("\n\n")
    instructions = list(letters)

    # process nodes
    for node in nodes_raw.split("\n"):
        process_node(start_nodes, nodes, node)

    # game
    for sn in start_nodes:
        score_start_nodes.append(get_first_appear(sn, instructions, nodes))

    # final score
    print(math.lcm(*score_start_nodes))


if __name__ == "__main__":
    main()
