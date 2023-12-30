from pprint import pprint

with open("data.txt", encoding="ascii") as f:
    steps = f.read().replace("\n", "").split(",")


def aoc_hash(string):
    total = 0
    for s in string:
        total = ((total + ord(s)) * 17) % 256
    return total


hashed = [aoc_hash(step) for step in steps]
print("Solution 1: " + str(sum(hashed)))

boxes = {i: [] for i in range(256)}
for step in steps:
    label = step.split("=")[0].replace("-", "")
    box_id = aoc_hash(label)
    if "=" in step:
        focal = int(step.split("=")[1])
        for lens in boxes[box_id]:
            if lens[0] == label:
                lens[1] = focal
                # print(box_id, label, focal, "changed")
                break
        else:  # for/else clause only executes if no breaks occurred ie label does not currently exist in box
            # print(box_id, label, focal, "added")
            boxes[box_id].append([label, focal])
    elif "-" in step:
        for l_id, lens in enumerate(boxes[box_id]):
            if lens[0] == label:
                boxes[box_id].pop(l_id)
                # print(box_id, label, "removed")
                break

total = 0
for box_id in range(256):
    for l_id, lens in enumerate(boxes[box_id]):
        total += (box_id + 1) * (l_id + 1) * lens[1]

print("Solution 2:", total)
