import networkx as nx

# CONSTANTS
FOREST = "#"
PATH = "."


def add_point(graph: nx.DiGraph, grid, curr_point: tuple[int, int], end_point: tuple[int, int]):
    # check for point out of bounds
    if 0 > end_point[0] > len(grid) or 0 > end_point[1] > len(grid[0]):
        return

    if end_point in graph:
        graph.add_edge(curr_point, end_point)


def clean_hill(graph: nx.DiGraph, grid, curr_point: tuple[int, int]):
    element = graph[curr_point[0]][curr_point[1]]


def main():
    G = nx.DiGraph
    start_point = None

    grid = []

    # place into array for traversal
    for row in open("data.txt").read().split("\n"):
        r = []
        for col in row:
            r.append(col)
        grid.append(r)

    # add points to Graph
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            # element
            element = grid[row_num][col_num]

            # check for forest tile
            if element == FOREST:
                continue

            # check for no start point
            elif not start_point and element == PATH:
                start_point = (row_num, col_num)
                G.add_node((row_num, col_num))

            else:
                G.add_node((row_num, col_num))

    # add

    print(grid)


if __name__ == '__main__':
    main()
