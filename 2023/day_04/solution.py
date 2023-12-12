
data = list()
with open("data.txt") as f:
    for line in f:
        clean = line.split(": ")[1].strip().replace("  ", " ")
        data.append(clean)

point_total = 0
copies_dict = {c: 1 for c in range(len(data))}

for index, item in enumerate(data):
    cards = item.split(" | ")

    win_set = {int(num) for num in cards[0].split(" ")}
    you_set = {int(num) for num in cards[1].split(" ")}

    matches = len(win_set.intersection(you_set))

    if matches:
        point_total += 2 ** (matches - 1)

        for i in range(matches, 0, -1):
            copies_dict[index + i] = copies_dict.get(index + i, 0) + copies_dict.get(index, 1)

copies_tptal = sum(copies_dict.values())

print("Solution 1: " + str(point_total))
print("Solution 2: " + str(copies_tptal))