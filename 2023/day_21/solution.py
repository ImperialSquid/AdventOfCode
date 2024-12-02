from pprint import pp

grid = []
with open("data.txt") as f:
    for l_id, line in enumerate(f):
        grid.append(line.strip())
        if "S" in line:
            start = (l_id, line.index("S"))

grid_w = len(grid)
compass = ((0, 1), (0, -1), (1, 0), (-1, 0))


def part1_garden_walk(steps, expand=False):
    to_step = [start, ]
    visited = dict()

    max_steps = max(steps)
    for s in range(max_steps + 1):
        visited[s] = []
        next_step = set()

        for tile in to_step:
            visited[s].append(tile)

            for dir in compass:
                new_r = tile[0] + dir[0]
                new_c = tile[1] + dir[1]
                if expand and -1 < (new_r % grid_w) < grid_w and -1 < (new_c % grid_w) < grid_w \
                        and grid[(new_r % grid_w)][(new_c % grid_w)] != "#":  # infinite grid expansion for part 2
                    next_step.add((new_r, new_c))
                elif -1 < new_r < grid_w and -1 < new_c < grid_w and grid[new_r][new_c] != "#":
                    next_step.add((new_r, new_c))
        to_step = list(next_step)

        if s + 1 in steps:
            print("Yielded: ", s + 1, len(visited[s]))
            yield len(visited[s])  # save work for part 2 by yielding rather than returning


def part2_garden_walk():
    # # See part2.md for an explanation of the logic going on here and the derivation of these equations
    # j = 65
    # k = 131
    #
    # steps = [j, j + k, j + k * 2]
    # tiles = list(part1_garden_walk(steps, expand=True))
    #
    # x1, x2, x3 = steps
    # y1, y2, y3 = tiles

    x1, x2, x3 = [65, 196, 327]
    y1, y2, y3 = [3729, 33970, 94573]

    a = y1 / ((x1 - x2) * (x1 - x3)) + \
        y2 / ((x2 - x1) * (x2 - x3)) + \
        y3 / ((x3 - x1) * (x3 - x2))

    b = -y1 * (x2 + x3) / ((x1 - x2) * (x1 - x3)) + \
        -y2 * (x1 + x3) / ((x2 - x1) * (x2 - x3)) + \
        -y3 * (x1 + x2) / ((x3 - x1) * (x3 - x2))

    c = y1 * x2 * x3 / ((x1 - x2) * (x1 - x3)) + \
        y2 * x1 * x3 / ((x2 - x1) * (x2 - x3)) + \
        y3 * x1 * x2 / ((x3 - x1) * (x3 - x2))

    print(a, b, c)
    print([a * x ** 2 + b * x + c for x in [65, 196, 327]])
    for s in [6, 10, 50, 100, 500, 1000, 5000, 65, 196, 327, 26501365]:
        print(s, a * s ** 2 + b * s + c)

    return a * 26501365 ** 2 + b * 26501365 + c


# pp(visited)
print("Solution 1: ", list(part1_garden_walk([10, 50, 64, 100, 500], expand=False))[0])
print("Solution 2: ", part2_garden_walk())
