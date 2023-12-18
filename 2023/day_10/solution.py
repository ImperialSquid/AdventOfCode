from re import findall

grid = list()
with open("data.txt") as f:
    for i, line in enumerate(f):
        grid.append(list(line.strip()))
        if "S" in line:
            start = [i, line.index("S")]

# Find first step
prev = [start[0], start[1]]
if start[0] > 0 and grid[start[0] - 1][start[1]] in ["7", "|", "F"]:
    # north
    curr = [start[0] - 1, start[1]]
elif start[1] < len(grid[0]) and grid[start[0]][start[1] + 1] in ["7", "-", "J"]:
    # east
    curr = [start[0], start[1] + 1]
elif start[0] < len(grid) and grid[start[0] + 1][start[1]] in ["L", "|", "J"]:
    # south
    curr = [start[0] + 1, start[1]]
elif start[1] > 0 and grid[start[0]][start[1] - 1] in ["L", "-", "F"]:
    # west
    curr = [start[0], start[1] - 1]
else:
    raise ValueError()

# Navigate loop back to start
loop = [[start[0], start[1]]]
while curr != start:
    loop.append([curr[0], curr[1]])

    if grid[curr[0]][curr[1]] == "|":
        if curr[0] + 1 == prev[0]:
            prev[0] -= 1
            curr[0] -= 1
        else:
            prev[0] += 1
            curr[0] += 1
    elif grid[curr[0]][curr[1]] == "-":
        if curr[1] + 1 == prev[1]:
            prev[1] -= 1
            curr[1] -= 1
        else:
            prev[1] += 1
            curr[1] += 1
    elif grid[curr[0]][curr[1]] == "J":
        if curr[0] - 1 == prev[0]:
            prev[0] += 1
            curr[1] -= 1
        else:
            prev[1] += 1
            curr[0] -= 1
    elif grid[curr[0]][curr[1]] == "F":
        if curr[1] + 1 == prev[1]:
            prev[1] -= 1
            curr[0] += 1
        else:
            prev[0] -= 1
            curr[1] += 1
    elif grid[curr[0]][curr[1]] == "L":
        if curr[0] - 1 == prev[0]:
            prev[0] += 1
            curr[1] += 1
        else:
            prev[1] -= 1
            curr[0] -= 1
    elif grid[curr[0]][curr[1]] == "7":
        if curr[1] - 1 == prev[1]:
            prev[1] += 1
            curr[0] += 1
        else:
            prev[0] -= 1
            curr[1] -= 1

print("Solution 1: " + str(len(loop) // 2))

# Grid of Unknown and Loop Tiles
enclosed = []
for i in range(len(grid)):
    enclosed.append([])
    for j in range(len(grid[0])):
        if [i, j] in loop:
            enclosed[-1].append(grid[i][j])
        elif i == 0 or j == 0 or i == len(grid) or i == len(grid[0]):
            enclosed[-1].append("O")
        else:
            enclosed[-1].append("U")


for i, row in enumerate(enclosed):
    for j, chr in enumerate(row):
        if chr != "U":
            continue

        # Count inside/outside parity to the left of current tile
        # TODO: do adjacency scanning for most of grid, regex for surrounded tiled that are actually Outside
        #  performing regex for every Unsolved tile is probably not efficient
        if len(findall("[FS]-*[JS]|[LS]-*[7S]|[|S]", "".join(row[:j]))) % 2 == 1:
            enclosed[i][j] = "I"
        else:
            enclosed[i][j] = "O"

# print("\n".join(["".join(row) for row in enclosed]))

enc_count = "".join(["".join(row) for row in enclosed]).count("I")

print("Solution 2: " + str(enc_count))
