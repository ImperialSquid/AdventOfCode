from pprint import pprint
from functools import cache

with open("data.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]

@cache
def tilt_west(grid):
    tilted_grid = []
    for i, row in enumerate(grid):
        row = "".join(row)
        tilted = ""
        for s in row.split("#"):
            tilted += s.count("O") * "O"
            tilted += s.count(".") * "."
            tilted += "#"
        tilted_grid.append(tilted[:-1])
    return tilted_grid


def tuplise(grid):  # lists are not compatible with @cache, convert to tuple
    return tuple([tuple(row) for row in grid])


def tilt(grid, dir = 0):
    # 0 north, 1 west, 2 south, 3 east
    if dir % 2 == 0: # flip N -> W, S -> E
        grid = list(zip(* grid))
    if dir // 2 == 1:  # flip  E -> W
        grid = [list(reversed(row)) for row in grid]

    grid = tilt_west(tuplise(grid))

    if dir // 2 == 1:
        grid = [list(reversed(row)) for row in grid]
    if dir % 2 == 0:
        grid = list(zip(* grid))

    return grid


def tilt_cycle(grid):
    for i in range(4):
        grid = tilt(grid, dir=i)
    return grid


tilt_grid = tilt(grid, dir=0)
tilt_total = sum([(i+1) * "".join(row).count("O")
                  for i, row in enumerate(reversed(tilt_grid))])
print("solution 1: " + str(tilt_total))


prev_grids = {}
cycle_num = 0
for i in range(1000000000):
    grid = tilt_cycle(grid)

    # print(i)
    # print("\n".join(["".join(row) for row in grid]))

    if prev_grids.get(tuplise(grid), None) is not None:
        m = prev_grids[tuplise(grid)]  # first occurrence of current grid
        cycle_num = (15 - m) % (i - m + 1) + 1
        print(i)
        print((15 - m) % (i - m + 1) + 1)
        print(m)
        final_grid = [k for k in prev_grids if prev_grids[k] == cycle_num][0]
        pprint(final_grid)
        break
    else:
        prev_grids[tuplise(grid)] = i

tilt_cycle_total = sum([(i+1) * "".join(row).count("O")
                        for i, row in enumerate(reversed(final_grid))])
print("Solution 2: " + str(tilt_cycle_total))
