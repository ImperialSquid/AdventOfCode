from collections import Counter

data = list()
with open("data.txt") as f:
    for line in f:
        splits = line.split(" ")
        data.append((splits[0], int(splits[1])))

normal_values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
wildcard_values = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def normal_hands(hand):
    occurances = list(Counter(hand).values())
    occurances.sort()

    return occurances

def wildcard_hands(hand):
    counter = Counter(hand)

    J_count = counter["J"]  # preserve J count but exclude from normal sort
    del counter["J"]

    occurances = list(counter.values())
    occurances.sort()

    # add J's to whatever card occurs most guarantees strongest conversion
    if len(occurances) > 0:
        occurances[-1] += J_count
    else:
        occurances = [5, ]  # special case for all Js

    return occurances

def hand_sort(hand, game_type, card_values):
    value = 0

    occurances = game_type(hand)
    if occurances == [1, 1, 1, 1, 1]:  # high card
        value += 1
    elif occurances == [1, 1, 1, 2]:  # one pait
        value += 2
    elif occurances == [1, 2, 2]:  # two [air
        value += 3
    elif occurances == [1, 1, 3]:  # 3 of a kind
        value += 4
    elif occurances == [2, 3]:  # full house
        value += 5
    elif occurances == [1, 4]:  # 4 of a kind
        value += 6
    elif occurances == [5]:  # 5 of a kind
        value += 7
    else:
        raise ValueError(hand, occurances)
    value *= 1000 ** 5

    for index, card in enumerate(hand):
        value += (1000 ** (4 - index)) * (card_values.index(card) + 1)

    return value

normal_sorted = sorted(data, key=lambda hand: hand_sort(hand[0], normal_hands, normal_values))
normal_winningss = sum([hand[1] * (i+1) for i, hand in enumerate(normal_sorted)])

wildcard_sorted = sorted(data, key=lambda hand: hand_sort(hand[0], wildcard_hands, wildcard_values))
wildcard_winningss = sum([hand[1] * (i+1) for i, hand in enumerate(wildcard_sorted)])


print("Solution 1: " + str(normal_winningss))
print("Solution 2: " + str(wildcard_winningss))
