START_NODE = "AAA"
END_NODE = "ZZZ"


def process_node(nodes: dict, raw: str):
    # split
    start_node, end_nodes = raw.split(" = ")

    # formatting
    l_raw, r_raw = end_nodes.split(", ")
    l_raw = l_raw.replace("(", "")
    r_raw = r_raw.replace(")", "")

    # put into nodes
    nodes[start_node] = [l_raw, r_raw]

def main():
    # vars
    instructions: list[str]
    nodes = dict()
    score = 0

    # pull data from file
    letters, nodes_raw = open("data.txt").read().split("\n\n")
    instructions = list(letters)

    # process nodes
    for node in nodes_raw.split("\n"):
        process_node(nodes, node)

    # game
    curr_node = START_NODE
    while curr_node != END_NODE:
        for i in instructions:
            score += 1
            node_list = nodes[curr_node]

            # move nodes
            if i == "L":
                curr_node = node_list[0]
            else:
                curr_node = node_list[1]

            # quit if end
            if curr_node == END_NODE:
                print(score)
                return


if __name__ == "__main__":
    main()
