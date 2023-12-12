import re

with open("data.txt") as f:
    total = 0

    for line in f:
        first = re.search("^[^0-9]*([0-9])", line).group(1)
        last = re.search("([0-9])[^0-9]*$", line).group(1)

        total += int(first+last)

    print(f"Solution 1: {total}")

with open("data.txt") as f:
    total = 0

    convert_dict = {str(x): str(x) for x in range(10)}
    convert_dict["zero"] = "0" # there's probably a better way to do this ;p;
    convert_dict["one"] = "1"
    convert_dict["two"] = "2"
    convert_dict["three"] = "3"
    convert_dict["four"] = "4"
    convert_dict["five"] = "5"
    convert_dict["six"] = "6"
    convert_dict["seven"] = "7"
    convert_dict["eight"] = "8"
    convert_dict["nine"] = "9"

    for line in f:
        first = re.search("([0-9]|one|two|three|four|five|six|seven|eight|nine|zero).*", line).group(1)
        last = re.search(".*([0-9]|one|two|three|four|five|six|seven|eight|nine|zero)", line).group(1)

        total += int(convert_dict[first]+convert_dict[last])

    print(f"Solution 2: {total}")
