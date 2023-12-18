from re import finditer, search
from functools import cache

springs = []
records = []
quint_springs = []
quint_records = []
with open("data.txt") as f:
    for line in f:
        s, r = line.strip().split(" ")
        springs.append(s)
        records.append(tuple([int(num) for num in r.split(",")]))

        quint_springs.append(s + ("?" + s) * 4)
        quint_records.append(tuple([int(num) for num in r.split(",") * 5]))


# print(springs)
# print(records)

@cache  # jesus this took foreverwithout cacheing
def all_poss(springs, records):  # , solution = None):
    if len(records) == 0 and "#" in springs:
        return 0  # no remaining hints with remainign springs = invalid
    elif len(records) == 0:
        return 1  # no remaining hints and no extra springs = 1 possible match

    if len(springs) < sum(records) + len(records) - 1:
        return 0  # remaining sectios cannot fit

    total = 0
    if search("(?=" + "[#?]" * records[0] + "(\.|\?|$))", springs):
        for match in finditer("(?=" + "[#?]" * records[0] + "(\.|\?|$))", springs):
            if "#" in springs[:match.span()[0]]:  # all springs must be part of groups
                continue  # skip further solving since results would be invalid
            # print(records, springs, match, springs[:match.span()[0] + records[0]])

            new_springs = springs[match.span()[0] + records[0] + 1:]
            total += all_poss(new_springs, records[1:])  # , solution + "." * match.span()[0] + "#" * records[0] + ".")
        return total
    else:
        return 0  # not possible to fit remaining section, return 0


all_poss_sum = sum([all_poss(springs[i], records[i]) for i in range(len(springs))])
print("Solution 1: " + str(all_poss_sum))

quint_all_poss_sum = sum([all_poss(quint_springs[i], quint_records[i]) for i in range(len(springs))])
print("Solution 2: " + str(quint_all_poss_sum))
