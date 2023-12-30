with open("data.txt") as f:
    grid = [list(l) for l in f.read().splitlines()]


def find_energised(r, c, d):
    energised = [["." for c in range(len(grid[0]))] for r in range(len(grid))]

    # puzzle can be formulated as a graph traversal problem, solving in a breadth first search style
    beams = [[r, c, d], ]  # tracks beam heads [row, col, dir] (north is 0)
    seen = []  # avoid duplication of work (and infinite loops)

    while len(beams) > 0:
        r, c, d = beams.pop(0)
        if [r, c, d] in seen:  # skip already processed tiles
            continue
        seen.append([r, c, d])

        energised[r][c] = "#"

        to_add = []
        tile = grid[r][c]
        if tile == "." or tile == "-" and d % 2 == 1 or tile == "|" and d % 2 == 0:
            r += ((d+1) % 2) * (d - 1)  # adjust r after transformed d, 0 -> -1, 2 -> 1, 1,3 - > 0
            c += (d % 2) * (-1 * d + 2)  # 1 -> 1, 3 -> -1, 0,2 - > 0
            to_add.append([r, c, d])
        elif tile == "/" and d == 1 or tile == "\\" and d == 3:  # refl north
            to_add.append([r-1, c, 0])
        elif tile == "/" and d == 0 or tile == "\\" and d == 2:  # refl east
            to_add.append([r, c+1, 1])
        elif tile == "/" and d == 3 or tile == "\\" and d == 1:  # refl south
            to_add.append([r+1, c, 2])
        elif tile == "/" and d == 2 or tile == "\\" and d == 0:  # refl west
            to_add.append([r, c-1, 3])
        elif tile == "|":  # splits are the same regardless of input dir
            to_add.append([r-1, c, 0])
            to_add.append([r+1, c, 2])
        elif tile == "-":
            to_add.append([r, c+1, 1])
            to_add.append([r, c-1, 3])
        else:
            raise ValueError()

        for a in to_add:
            if -1 < a[0] < len(grid) and -1 < a[1] < len(grid[0]):  # beam is not off grid
                beams.append(a)

    return "".join(["".join(row) for row in energised]).count("#")


print("Solution 1:", find_energised(r=0, c=0, d=1))

# could absolutely be optimised eg by keeping track of known loops and skipping them if they are encountered
# but each solve takes approx 2 secs so brute force will do lol
energised_max = 0
for d in range(4):
    if d == 0:
        for c in range(len(grid[0])):
            new = find_energised(r=len(grid) - 1, c=c, d=d)
            energised_max = max(energised_max, new)
            print(len(grid) - 1, c, d, energised_max, new)
    elif d == 1:
        for r in range(len(grid)):
            new = find_energised(r=r, c=0, d=d)
            energised_max = max(energised_max, new)
            print(r, 0, d, energised_max, new)
    elif d == 2:
        for c in range(len(grid[0])):
            new = find_energised(r=0, c=c, d=d)
            energised_max = max(energised_max, new)
            print(0, c, d, energised_max, new)
    elif d == 3:
        for r in range(len(grid)):
            new = find_energised(r=r, c=len(grid[0]) - 1, d=d)
            energised_max = max(energised_max, new)
            print(r, len(grid[0]) - 1, d, energised_max, new)

print("Solution 2:", energised_max)
