from typing import Tuple

lower_bound = 200000000000000
upper_bound = 400000000000000


class Hail:
    x: int
    y: int

    x_v: int
    y_v: int

    def __init__(self, in_str: str):
        pos, vel = in_str.split(" @ ")
        pos = pos.split(", ")
        vel = vel.split(", ")

        self.x = int(pos[0])
        self.y = int(pos[1])

        self.x_v = int(vel[0])
        self.y_v = int(vel[1])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.x_v == other.x_v and self.y_v == other.y_v


def check_intersection_2(h1: Hail, h2: Hail) -> bool | tuple[float, float]:
    # Calculate the denominator
    denominator = (h1.x_v * h2.y_v - h2.x_v * h1.y_v)

    # If the denominator is zero, the lines are parallel and do not intersect
    if denominator == 0:
        return False

    # Calculate the intersection point
    u = ((h2.x - h1.x) * h2.y_v - (h2.y - h1.y) * h2.x_v) / denominator
    v = ((h2.x - h1.x) * h1.y_v - (h2.y - h1.y) * h1.x_v) / denominator

    # Return the intersection point
    return u, v


def check_intersection(h1: Hail, h2: Hail) -> bool | tuple[float, float]:
    x = h2.x - h1.x
    y = h2.y - h1.y

    d = h2.x * h1.y - h2.y * h1.x

    if d == 0:
        return False

    u = (y * h2.x - x * h2.y) / d
    v = (y * h1.x - x * h1.y) / d

    return u, v


def main():
    curr_hail = []
    score = 0

    for items in open("data.txt").read().split("\n"):
        curr_hail.append(Hail(items))

    for h1 in curr_hail:
        for h2 in curr_hail:

            # check for equal
            if h1 == h2:
                continue

            # get answer
            ans = check_intersection_2(h1, h2)
            print(ans)

            # check for no intersection
            if not ans:
                continue

            # check for within val
            if lower_bound <= ans[0] <= upper_bound and lower_bound <= ans[1] <= upper_bound:
                print("VALID " + str(ans))
                score += 1

    print(score / 2)


if __name__ == '__main__':
    main()
