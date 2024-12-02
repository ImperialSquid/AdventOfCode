reports = []

with open("data.txt") as f:
    for line in f:
        levels = line.strip().split()
        reports.append([int(l) for l in levels])

# pprint(reports)

def safe_report(report: list[int]) -> bool:
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]

    # check all diffs are at least 1 and at most 3 apart
    safe_level = all(list(map(lambda x: 1 <= abs(x) <= 3, diffs)))

    # check if diffs are all positive or all negative
    pos_diffs = list(map(lambda x: x > 0, diffs))
    neg_diffs = list(map(lambda x: x < 0, diffs))
    monotonic = all(pos_diffs) or all(neg_diffs)

    return safe_level and monotonic

# === part 1 & 2

p1_total = 0
p2_total = 0

for report in reports:
    if safe_report(report):
        p1_total += 1
        p2_total += 1
    else:
        for i in range(len(report)):
            partial_report = report[:i] + report[i+1:]
            if safe_report(partial_report):
                p2_total += 1
                break

print(f"Part 1 Solution: { p1_total }")
print(f"Part 2 Solution: { p2_total }")