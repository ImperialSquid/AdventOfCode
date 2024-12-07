from collections import defaultdict

map_area = defaultdict(lambda: "E")
orig_pos = complex("0+0j")
orig_dir = complex("-1")

with open("data.txt") as f:
    for l_index, line in enumerate(f.readlines()):
        for c_index, char in enumerate(line.strip()):
            map_area[complex(f"{l_index}+{c_index}j")] = char
            if char == "^":
                orig_pos = complex(f"{l_index}+{c_index}j")
                map_area[orig_pos] = "."


def walk(map_, walk_pos, walk_dir):
    visited_pos = {walk_pos}
    visited_pos_dir = {(walk_pos, walk_dir)}

    i = 0
    while True:
        i += 1

        next_pos = walk_pos + walk_dir

        if (next_pos, walk_dir) in visited_pos_dir:
            found_loop = True
            break

        next_tile = map_[next_pos]
        if next_tile == ".":
            walk_pos = next_pos
            visited_pos.add(walk_pos)
            visited_pos_dir.add((walk_pos, walk_dir))
        elif next_tile == "#":
            walk_dir *= complex("-1j")
        elif next_tile == "E":
            found_loop = False
            break

    return visited_pos, found_loop

visited, _ = walk(map_area, orig_pos, orig_dir)
p1_total = len(visited)

print(f"Part 1 Solution: { p1_total }")

# === part 2

p2_total = 0

for v in visited:
    # print(v)
    new_area = defaultdict(lambda: "E")
    new_area.update(map_area)
    new_area.update({v: "#"})

    _, loop = walk(new_area, orig_pos, orig_dir)

    if loop:
        p2_total += 1

print(f"Part 2 Solution: { p2_total }")
