from copy import deepcopy

workflows = dict()
parts = []

with open("data.txt") as f:
    for line in f:
        if line == "\n":  # workflows all read in
            break

        name, steps = line.strip()[:-1].split("{")
        instructions = []
        for step in steps.split(","):
            if ":" not in step:
                step = True if step == "A" else step
                step = False if step == "R" else step
                instructions.append((step,))
            else:
                split, result = step.split(":")

                cat = split[0]
                mult_f = 1 if split[1] == "<" else -1  # reverse inenqualities by negative mult
                num = int(split[2:])
                result = True if result == "A" else result
                result = False if result == "R" else result

                # None means test did not pass, True means accepted, False means rejected,
                # and any string means go to new workflow
                instructions.append((cat, mult_f, num, result))

        workflows[name] = instructions

    for line in f:
        part = {cat[0]: int(cat[2:]) for cat in line.strip()[1:-1].split(",")}
        parts.append(part)


def process_part(part, process):
    if len(process) == 1:
        return process[0]
    else:
        cat, mult_f, num, result = process
        return result if part[cat] * mult_f < num * mult_f else None


def split_part_range(part, process):
    if len(process) == 1:
        return [[process[0], part], ]
    else:
        cat, mult_f, num, result = process

        match = deepcopy(part)
        fail = deepcopy(part)

        if mult_f == 1:
            match[cat][1] = num - 1
            fail[cat][0] = num
        else:
            match[cat][0] = num + 1
            fail[cat][1] = num

        return [[result, match], [None, fail]]


accepted = []
for part in parts:
    r = "in"
    while r is not True and r is not False:  # run until rejected or accepted
        for process in workflows[r]:
            r = process_part(part, process)
            if r is not None:
                # print(r)
                break

    if r:
        accepted.append(part)

print("Solution 1:", sum([a["x"] + a["m"] + a["a"] + a["s"] for a in accepted]))

queue = [["in", {cat: [1, 4000] for cat in "xmas"}], ]
acc_ranges = []

while queue:
    wf, part_range = queue.pop(0)

    for process in workflows[wf]:
        splits = split_part_range(part_range, process)

        for split in splits:
            if split[0] is True:
                acc_ranges.append(split[1])
            elif split[0] is False:
                pass
            elif split[0] is None:
                part_range = split[1]
            else:
                queue.append(split)

part_combos = [(p["x"][1] - p["x"][0] + 1) *
               (p["m"][1] - p["m"][0] + 1) *
               (p["a"][1] - p["a"][0] + 1) *
               (p["s"][1] - p["s"][0] + 1) for p in acc_ranges]

print("Solutions 2: ", sum(part_combos))
