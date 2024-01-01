from itertools import pairwise, accumulate

with open("data.txt") as f:
    data = f.read().splitlines()


# TODO part 1 and 2 parsing could be combined, but it's solved now
def parse_part1(line):
    direction, distance, _ = line.split()
    delta = int(distance)
    return ((0, -delta), (delta, 0), (0, delta), (-delta, 0))['URDL'.index(direction)]


def parse_part2(line):
    _, _, colour = line.split()
    delta = int(colour[2:7], 16)
    return ((delta, 0), (0, delta), (-delta, 0), (0, -delta))[int(colour[7])]


def dig(inst):
    xs, ys = zip(*inst)  # separate out x and y
    xs = accumulate(xs)  # get each pos relative to the last
    ys = accumulate(ys)
    xy = list(zip(xs, ys))  # repackage back into pairs
    # print(xy)

    # shoelace formula to get double the internal areas
    double_area = sum(x1 * y2 - y1 * x2 for (x1, y1), (x2, y2) in pairwise(xy + xy[:1]))
    boundary = sum(abs(x2 - x1 + y2 - y1) for (x1, y1), (x2, y2) in pairwise(xy + xy[:1]))

    # use Pick's to derive actual area with boundary
    return (double_area + boundary) // 2 + 1


part1_inst = map(parse_part1, data)
part2_inst = map(parse_part2, data)

print("Solution 1:", dig(part1_inst))
print("Solution 2:", dig(part2_inst))
