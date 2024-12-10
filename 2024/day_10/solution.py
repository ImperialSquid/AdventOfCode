from pprint import pprint

with open("data.txt") as f:
    grid = [[int(char) if char != "." else -1 for char in line] for line in f.read().splitlines()]

trail_heads = [(l_i, c_i)
               for l_i, line in enumerate(grid)
               for c_i, char in enumerate(line)
               if grid[l_i][c_i] == 0]

print("\n".join(["".join([str(c) if c >= 0 else "." for c in l]) for l in grid]))
# print(trail_heads)

def walk_trail(line, char, step, th):
    if grid[line][char] == 9 and step == 9:
        peaks[th].append((line, char))
        return

    cell = grid[line][char]

    if 0 <= line + 1 < len(grid) and 0 <= char < len(grid[0]) and grid[line + 1][char] == cell + 1:
        walk_trail(line + 1, char, step + 1, th)
    if 0 <= line - 1 < len(grid) and 0 <= char < len(grid[0]) and grid[line - 1][char] == cell + 1:
        walk_trail(line - 1, char, step + 1, th)
    if 0 <= line < len(grid) and 0 <= char + 1 < len(grid[0]) and grid[line][char + 1] == cell + 1:
        walk_trail(line, char + 1, step + 1, th)
    if 0 <= line < len(grid) and 0 <= char - 1 < len(grid[0]) and grid[line][char - 1] == cell + 1:
        walk_trail(line, char - 1, step + 1, th)

    return


peaks = {}

for th in trail_heads:
    peaks[th] = []
    walk_trail(th[0], th[1], 0, th)

# pprint(peaks)

p1_total = sum([len(set(peak)) for peak in peaks.values()])
p2_total = len([p for peak in peaks.values() for p in peak])

print(f"Part 1 Solution: { p1_total }")
print(f"Part 2 Solution: { p2_total }")
