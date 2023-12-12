import networkx as nx
import networkx.exception


def next_node(visited_nodes: list, edges: list):
    for edge in edges:
        if edge[0] not in visited_nodes:
            return edge[0]
        if edge[1] not in visited_nodes:
            return edge[1]
    print(edges)


def get_longest_path(G: networkx.Graph, start_loc) -> int:
    cont = True
    visited = []
    currNode = start_loc
    print(G.edges(currNode))
    while cont:
        # add curr node to visited
        visited.append(currNode)

        # get edges
        currNode = next_node(visited, G.edges(currNode))

        if currNode is None:
            print(visited)
            cont = False

    return len(visited) // 2


def main():
    max_score = 0
    G = nx.Graph()
    start_loc: tuple[int, int] = (-1, -1)

    row_num = 0
    for row in open("data.txt").read().split("\n"):
        col_num = 0
        for char in row:
            # make four corner nodes
            G.add_node((row_num, col_num))

            # add pipe
            match char:
                case "|":
                    G.add_edge((row_num - 1, col_num), (row_num, col_num))
                    G.add_edge((row_num, col_num), (row_num + 1, col_num))
                case "-":
                    G.add_edge((row_num, col_num - 1), (row_num, col_num))
                    G.add_edge((row_num, col_num), (row_num, col_num + 1))
                case "L":
                    G.add_edge((row_num - 1, col_num), (row_num, col_num))
                    G.add_edge((row_num, col_num), (row_num, col_num + 1))
                case "J":
                    G.add_edge((row_num - 1, col_num), (row_num, col_num))
                    G.add_edge((row_num, col_num), (row_num, col_num - 1))
                case "7":
                    G.add_edge((row_num + 1, col_num), (row_num, col_num))
                    G.add_edge((row_num, col_num), (row_num, col_num - 1))
                case "F":
                    G.add_edge((row_num + 1, col_num), (row_num, col_num))
                    G.add_edge((row_num, col_num), (row_num, col_num + 1))
                case "S":
                    start_loc = (row_num, col_num)
                    G.add_edge((row_num + 1, col_num), (row_num, col_num))
                    G.add_edge((row_num - 1, col_num), (row_num, col_num))
                    G.add_edge((row_num, col_num + 1), (row_num, col_num))
                    G.add_edge((row_num, col_num - 1), (row_num, col_num))

            col_num += 1
        row_num += 1

    # traverse through loop
    print(get_longest_path(G, (start_loc[0], start_loc[1])))
    print(get_longest_path(G, (start_loc[0] + 1, start_loc[1])))
    print(get_longest_path(G, (start_loc[0] - 1, start_loc[1])))
    print(get_longest_path(G, (start_loc[0], start_loc[1] + 1)))
    print(get_longest_path(G, (start_loc[0], start_loc[1] - 1)))



if __name__ == "__main__":
    main()
