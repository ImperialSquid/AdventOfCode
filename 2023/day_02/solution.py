with open("data.txt") as f:
    poss_id_total = 0
    power_total = 0

    for line in f:
        counts = {"red": 0, "green": 0, "blue": 0}
        id_, data = line.strip().split(": ")

        for game in data.split("; "):
            for colour in game.split(", "):
                counts[colour.split(" ")[1]] = max(counts[colour.split(" ")[1]],
                                                   int(colour.split(" ")[0]))

        if counts["red"] <= 12 and counts["green"] <= 13 and counts["blue"] <= 14:
            poss_id_total += int(id_.split(" ")[1])

        power_total += counts["red"] * counts["green"] * counts["blue"]

    print("Solution 1: " + str(poss_id_total))
    print("Solution 2: " + str(power_total))
