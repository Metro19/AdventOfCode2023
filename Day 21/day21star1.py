import copy

MAX_STEPS = 6
START_CHAR = "S"
FORBIDDEN_CHAR = "#"


# def BFS(curr_point: (int, int), board: list[list[str]], total_steps: int, winning_tiles: list[(int, int)], visited: list[(int, int)]):
#     # point visited
#     total_steps += 1
# 
#     # check for out of bounds
#     if curr_point[0] < 0 or curr_point[0] >= len(board):
#         return
# 
#     if curr_point[1] < 0 or curr_point[1] >= len(board[0]):
#         return
# 
# 
#     # check for forbidden point
#     if board[curr_point[0]][curr_point[1]] == FORBIDDEN_CHAR:
#         return
# 
#     if total_steps >= MAX_STEPS:
#         if curr_point not in winning_tiles:
#             winning_tiles.append(curr_point)
#         return
# 
#     if curr_point in visited:
#         return
# 
# 
#     # point visited
#     visited.append(curr_point)
# 
#     points_to_visit = [(curr_point[0] + 1, curr_point[1]),
#                        (curr_point[0] - 1, curr_point[1]),
#                        (curr_point[0], curr_point[1] + 1),
#                        (curr_point[0], curr_point[1] - 1)]
# 
#     for point in points_to_visit:
#         visited_points_copy = copy.deepcopy(visited)
#         BFS(point, board, total_steps, winning_tiles, visited_points_copy)


def main():
    board = []
    start_loc = (-1, -1)
    row_num = -1

    for row in open("data.txt").read().split("\n"):
        r = []
        row_num += 1

        # check for start
        if START_CHAR in row:
            start_loc = (row_num, row.find(START_CHAR))

        for char in row:
            r.append(char)
        board.append(r)

    points_to_visit = [start_loc]

    for _ in range(MAX_STEPS):
        new_points_to_visit = []

        for p in points_to_visit:

            # check for invalid point
            # check for out of bounds
            if p[0] < 0 or p[0] >= len(board):
                continue

            if p[1] < 0 or p[1] >= len(board[0]):
                continue

            # check for forbidden point
            if board[p[0]][p[1]] == FORBIDDEN_CHAR:
                continue

            p2v = [(p[0] + 1, p[1]),
                       (p[0] - 1, p[1]),
                       (p[0], p[1] + 1),
                       (p[0], p[1] - 1)]

            for p2 in p2v:
                if p2 not in new_points_to_visit:
                    new_points_to_visit.append(p2)

        points_to_visit = new_points_to_visit

    # filter invalid points
    final_points = []
    for p in points_to_visit:
        # check for invalid point
        # check for out of bounds
        if p[0] < 0 or p[0] >= len(board):
            continue

        if p[1] < 0 or p[1] >= len(board[0]):
            continue

        # check for forbidden point
        if board[p[0]][p[1]] == FORBIDDEN_CHAR:
            continue

        # add to final
        final_points.append(p)

    print(points_to_visit)
    print(len(points_to_visit))

if __name__ == '__main__':
    main()
