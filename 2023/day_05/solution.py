from pprint import pprint

conv_dict = dict()

with open("data.txt") as f:
    data = f.readline().strip().split(" ")[1:]
    prev_list_single = [int(num) for num in data]
    prev_list_pairs = [[int(data[i]), int(data[i]) + int(data[i + 1])] for i in range(0, len(data), 2)]

    conv_mode = ""
    conv_list = list()
    for line in f:
        if line == "\n":
            continue

        elif "-to-" in line:
            conv_mode = line.split("-to-")[0]
            conv_list.append(conv_mode)

        else:
            data = [int(num) for num in line.split(" ")]

            conv_dict[conv_mode] = conv_dict.get(conv_mode, list()) + \
                                   [[data[1], data[1] + data[2] - 1, data[0] - data[1]], ]
            #                      src start, src end,               src to dest offset

print(conv_list)
pprint(conv_dict)

print(prev_list_single)
pprint(prev_list_pairs)

print("\n\n------\n\n")

for mode in conv_list:
    next_list_single = [None for _ in range(len(prev_list_single))]
    next_list_pairs = list()

    print(prev_list_pairs)

    for conv in conv_dict[mode]:
        for index, item in enumerate(prev_list_single):
            if conv[0] <= item <= conv[1]:
                next_list_single[index] = item + conv[2]

        for index, item in enumerate(prev_list_pairs):
            if item[1] < conv[0] or conv[1] < item[0]:
                # test range is not within conversion range
                continue

            elif conv[0] <= item[0] and item[1] <= conv[1]:
                # test range is fully within conversion range
                next_list_pairs.append([item[0] + conv[2], item[1] + conv[2]])
                prev_list_pairs[index] = [-1_000_000_000, -1_000_000_000]

            elif item[0] < conv[0] and conv[1] < item[1]:
                # conversion hits part of rangw
                prev_list_pairs[index][1] = conv[0] - 1
                prev_list_pairs.append([conv[1] + 1, item[1]])

                next_list_pairs.append([conv[0] + conv[2], conv[1] + conv[2]])

            elif conv[0] <= item[0] and item[0] <= conv[1]:
                # test low end in conversion range
                next_list_pairs.append([item[0] + conv[2], conv[1] + conv[2]])
                prev_list_pairs[index][0] = conv[1] + 1

            elif conv[0] <= item[1] and item[1] <= conv[1]:
                # test high end in conversion range
                next_list_pairs.append([conv[0] + conv[2], item[1] + conv[2]])
                prev_list_pairs[index][1] = conv[0] - 1

            else:
                raise ValueError()

    for i in range(len(prev_list_single)):
        if next_list_single[i] is None:
            next_list_single[i] = prev_list_single[i]

    prev_list_single = next_list_single
    prev_list_pairs = next_list_pairs + [p for p in prev_list_pairs if p[0] > -1_000_000]

print(prev_list_pairs)

print("Soution 1: " + str(min(prev_list_single)))
print("Soution 2: " + str(min([v[0] for v in prev_list_pairs])))
