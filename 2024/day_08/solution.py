from collections import defaultdict
from itertools import combinations

antennas = defaultdict(list)

l_max = 0
c_max = 0

with open("data.txt") as f:
    for l_index, line in enumerate(f):
        l_max = max(l_max, l_index)
        for c_index, char in enumerate(line.strip()):
            c_max = max(c_max, c_index)
            if char != ".":
                antennas[char].append(complex(f"{l_index}+{c_index}j"))

p1_anti_nodes = set()
p2_anti_nodes = set()

for antenna in antennas:
    for a1, a2 in combinations(antennas[antenna], 2):
        dist = a2 - a1

        # generate a bunch of possible anti nodes in both directions
        ans1 = [a2 + dist * n for n in range(1, 100) if
                (0 <= (a2 + dist * n).real <= l_max)
                and (0 <= (a2 + dist * n).imag <= c_max)]
        ans2 = [a1 - dist * n for n in range(1, 100) if
                (0 <= (a1 - dist * n).real <= l_max)
                and (0 <= (a1 - dist * n).imag <= c_max)]

        # p1 only takes the first (slicing an empty list is fine)
        p1_anti_nodes |= {* ans1[:1]}
        p1_anti_nodes |= {* ans2[:1]}

        p2_anti_nodes |= {* ans1}
        p2_anti_nodes |= {* ans2}
        p2_anti_nodes |= {* [a1, a2]}  # "including every anti node *on* every antenna"

p1_total = len(p1_anti_nodes)
p2_total = len(p2_anti_nodes)

print(p2_anti_nodes)

print(f"Part 1 Solutions: { p1_total }")
print(f"Part 2 Solutions: { p2_total }")

# bonus: print all the anti nodes
# area = "\n".join(["".join(["#" if (complex(f"{l_i}+{c_i}j") in p2_anti_nodes) else "."
#                            for c_i in range(c_max+1) ])
#                   for l_i in range(l_max+1)])
#
# print(area)