from collections import Counter

left = []
right = []

with open("data.txt") as f:
    for line in f:
        l, r = line.strip().split()
        l = int(l)
        r = int(r)

        left.append(l)
        right.append(r)

        # print(line.strip().split())

# === part 1

left = sorted(left)
right = sorted(right)
p1_total = 0

for l, r in zip(left, right):
    p1_total += abs(l - r)

print(f"Part 1 Solution: { p1_total }")

# === part 2

counts = Counter(right)
p2_total = 0

for l in left:
    p2_total += l * counts[l]

print(f"Part 2 Solution: { p2_total }")