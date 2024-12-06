from collections import defaultdict

map_area = defaultdict(lambda: "E")
visited = {}
guard_pos = complex("0+0j")
guard_dir = complex("-1")

with open("data.txt") as f:
    for l_index, line in enumerate(f.readlines()):
        for c_index, char in enumerate(line.strip()):
            map_area[complex(f"{l_index}+{c_index}j")] = char
            visited[complex(f"{l_index}+{c_index}j")] = False
            if char == "^":
                guard_pos = complex(f"{l_index}+{c_index}j")
                map_area[guard_pos] = "."
                visited[guard_pos] = True

cur_tile = map_area[guard_pos]

while True:
    next_pos = guard_pos + guard_dir

    next_tile = map_area[next_pos]
    if next_tile == ".":
        guard_pos = next_pos
        visited[guard_pos] = True
    elif next_tile == "#":
        guard_dir *= complex("-1j")
    elif next_tile == "E":
        break

p1_total = sum([v for v in visited.values()])

print(f"Part 1 Solution: { p1_total }")