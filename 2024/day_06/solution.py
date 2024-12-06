from collections import defaultdict

map_area = defaultdict(lambda: defaultdict(lambda: "E"))
visited = {}
guard_pos = (-1, -1, 0)  # (row, col, dir)

with open("data.txt") as f:
    for l_index, line in enumerate(f.readlines()):
        map_area[l_index] = defaultdict(lambda: "E")
        visited[l_index] = {}
        for c_index, char in enumerate(line.strip()):
            map_area[l_index][c_index] = char
            visited[l_index][c_index] = False
            if char == "^":
                guard_pos = (l_index, c_index, 0)
                map_area[l_index][c_index] = "."
                visited[l_index][c_index] = True

cur_tile = map_area[guard_pos[0]][guard_pos[1]]

index = 0
while True:
    index += 1

    print(guard_pos)
    print(cur_tile)
    next_pos = (guard_pos[0] + ((guard_pos[2]+1) % 2) * -1 + int(guard_pos[2] == 2) * 2, # 0 -> -1, 2 -> 1, 1,3 -> 0
                guard_pos[1] + ((guard_pos[2]) % 2) * -1 + int(guard_pos[2] == 1) * 2)  # 1 -> 1, 3 -> -1, 0,2 -> 0

    # rows:
    #   0 -> Y + (1 % 2) * -1 + 0 * 2 = Y-1
    #   2 -> Y + (3 % 2) * -1 + 1 * 2 = Y+1
    # 1,3 -> Y + (0 % 2) * -1 + 0 * 2 = Y
    # cols:
    #   1 -> X + (1 % 2) * -1 + 1 * 2 = X+1
    #   3 -> X + (3 % 2) * -1 + 0 * 2 = X-1
    # 0,2 -> X = (0 % 2) * -1 + 0 * 2 = X

    next_tile = map_area[next_pos[0]][next_pos[1]]

    if next_tile == ".":
        guard_pos = (next_pos[0], next_pos[1], guard_pos[2])
        visited[guard_pos[0]][guard_pos[1]] = True
    elif next_tile == "#":
        guard_pos = (guard_pos[0], guard_pos[1], (guard_pos[2]+1) % 4)
    elif next_tile == "E":
        break

    if index % 10000 == 0:
        area = ""
        for l_i, line in visited.items():
            for c_i, char in line.items():
                if char:
                    area += "X"
                else:
                    area += map_area[l_i][c_i]
            area += "\n"
        print(area)
        input("Continue? ")

area = ""
for l_i, line in visited.items():
    area += str(l_i).zfill(3) + " - "

    for c_i, char in line.items():
        if char:
            area += "X"
        else:
            area += map_area[l_i][c_i]
    area += "\n"
print(area)
print(sum([sum([v for v in visit.values()]) for visit in visited.values()]))