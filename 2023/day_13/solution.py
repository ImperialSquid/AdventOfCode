from pprint import pprint

grids = [[], ]
with open("data.txt") as f:
    for line in f:
        if line == "\n":
            grids.append([])
            continue

        grids[-1].append([int(c == "#") for c in line.strip()])


def find_mirror(grid, diffs=0):
    for row_i in range(1, len(grid)):
        if sum([a != b  # count differences...
                for above, below in zip(reversed(grid[:row_i]), grid[row_i:])
                for a, b in zip(above, below)]) == diffs:  # ... zero diffs is a mirror
            return row_i
    return 0


p1_total = 0
p2_total = 0

for grid in grids:
    p1_total += find_mirror(grid, diffs=0) * 100
    p2_total += find_mirror(grid, diffs=1) * 100

    grid = list(zip(*grid))

    p1_total += find_mirror(grid, diffs=0)
    p2_total += find_mirror(grid, diffs=1)

print("Solution 1: " + str(p1_total))
print("Solution 2: " + str(p2_total))
