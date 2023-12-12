import re

lines = ["." * 1000]
with open("data.txt") as f:
    for line in f:
        lines.append("." + line.strip() + ".")
lines.append("." * 1000)  # padding for later scanning to avoid try/except block

id_total = 0
gear_dict = dict()

for index, line in enumerate(lines):
    for match in re.finditer("[0-9]+", line):
        num = int(match.group())
        span = match.span()

        text = lines[index - 1][span[0]-1: span[1]+1] + \
               lines[index][span[0]-1: span[1]+1] + \
               lines[index + 1][span[0]-1: span[1]+1]

        symbol = re.search("[^.0-9]", text)
        if symbol:
            id_total += num

            if symbol.group() == "*":
                # use relative offet to find gear absolute pos
                pos_off = symbol.start() % (span[1] - span[0] + 2) - 1
                inx_off = symbol.start() // (span[1] - span[0] + 2) - 1
                gear_pos = str(index + inx_off) + "-" + str(match.start() + pos_off)

                gear_dict[gear_pos] = gear_dict.get(gear_pos, list()) + [num, ]

print(gear_dict)

gear_ratio_sum = sum([v[0] * v[1] if len(v) == 2 else 0
                      for v in gear_dict.values()])

print("Solution 1: " + str(id_total))
print("Solution 2: " + str(gear_ratio_sum))
