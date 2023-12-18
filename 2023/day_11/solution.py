from itertools import combinations
from contextlib import suppress

star_grid = []
with open("data.txt") as f:
    for line in f:
        line = line.strip()
        star_grid.append(list(line))

galaxies = []
# rather than deal with massive nested lists just count how many times a route
# between galaxies crosses an empty r/c and multiply later
empty_cols = list(range(len(star_grid)))
empty_rows = list(range(len(star_grid[0])))

for i, row in enumerate(star_grid):
    for j, item in enumerate(row):
        if item == "#":
            galaxies.append([i, j])

            with suppress(ValueError):  # fewer lines than try/except + functionally same
                empty_cols.remove(i)
            with suppress(ValueError):
                empty_rows.remove(j)

# print("\n".join(["".join(row) for row in star_grid]))
# print(empty_cols)
# print(empty_rows)


def dist(a, b, exp_factor):
    total = abs(a[0] - b[0]) + abs(a[1] - b[1])

    empty_cols_btwn = list(filter(lambda x: min(a[0], b[0]) < x < max(a[0], b[0]),
                                  empty_cols))
    empty_rows_btwn = list(filter(lambda x: min(a[1], b[1]) < x < max(a[1], b[1]),
                                  empty_rows))

    total += (exp_factor - 1) * (len(empty_cols_btwn) + len(empty_rows_btwn))
    return total


# for a, b in combinations(galaxies, 2):
#     print(a, b , dist(a, b, 2))

double_sum = sum([dist(a, b, 2) for a, b in combinations(galaxies, 2)])
million_sum = sum([dist(a, b, 1000000) for a, b in combinations(galaxies, 2)])

print("Solution 1: " + str(double_sum))
print("Solution 2: " + str(million_sum))
