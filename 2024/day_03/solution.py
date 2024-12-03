import re

with open("data.txt") as f:
    lines = f.readlines()

# === part 1 & 2

p1_total = 0
p2_total = 0
mul_enabled = True

for line in lines:
    # match on either a mul(XX,YY) or do()/don't() statement
    # groups:
    #   0 - XX
    #   1 - YY
    #   2 - do()/don't()
    for match in re.finditer(r"mul\((\d+),(\d+)\)|(do(?:n\'t)?\(\))", line):
        if match.groups()[2]:
            mul_enabled = "do()" == match.groups()[2]
        else:
            p1_total += int(match.groups()[0]) * int(match.groups()[1])
            if mul_enabled:
                p2_total += int(match.groups()[0]) * int(match.groups()[1])

print(f"Part 1 Solution: { p1_total }")
print(f"Part 2 Solution: { p2_total }")