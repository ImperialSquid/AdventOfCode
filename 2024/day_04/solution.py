from collections import defaultdict


def get_input_data(file):
    ws_dict = defaultdict(lambda: defaultdict(lambda: '.'))

    with open(file, "r") as f:
        for l_index, line in enumerate(f.readlines()):
            ws_dict[l_index] = defaultdict(lambda: '.')
            for c_index, char in enumerate(line):
                ws_dict[l_index][c_index] = char

    return ws_dict


def get_words(ws_dict: dict[int, dict[int, str]], i: int, j: int, length: int):
    words = ["", "", "", ""]

    for l in range(length):
        words[0] += ws_dict[i][j + l]  # horizontally forward
        words[1] += ws_dict[i + l][j]  # vertically down
        words[2] += ws_dict[i + l][j + l]  # diagonally south-east
        words[3] += ws_dict[i + l][j - l]  # diagonally south-west

    return words


def find_x_mas(sw_dict, i, j):
    d1 = sw_dict[i - 1][j - 1] + sw_dict[i][j] + sw_dict[i + 1][j + 1]
    d2 = sw_dict[i + 1][j - 1] + sw_dict[i][j] + sw_dict[i - 1][j + 1]

    d1_true = d1 == "MAS" or d1 == "SAM"
    d2_true = d2 == "MAS" or d2 == "SAM"

    return d1_true and d2_true


def solve_p1(data):
    p1_total = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            # print(get_words(ws_dict, i, j, 4))
            words = get_words(data, i, j, 4)

            p1_total += sum(map(lambda x: x == "XMAS", words))
            p1_total += sum(map(lambda x: x == "SAMX", words))

    return p1_total


def solve_p2(data):
    p2_total = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if find_x_mas(data, i, j):
                p2_total += 1

    return p2_total


def main():
    data = get_input_data("data.txt")

    p1 = solve_p1(data)
    p2 = solve_p2(data)

    print(f"Part 1 Solution: { p1 }")
    print(f"Part 2 Solution: { p2 }")


if __name__ == "__main__":
    main()
