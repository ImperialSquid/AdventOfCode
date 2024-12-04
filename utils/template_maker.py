import os

year = input("AoC Year: ")
force_remake = input("Force remake? (y/n): ")

dirs = ([os.path.join("..", year), ] +
        [os.path.join("..", year, "day_"+str(day+1).zfill(2)) for day in range(25)])

for dir in dirs:
    if not os.path.exists(dir):
        os.mkdir(dir)

for day in dirs[1:]:
    data = os.path.join(day, "data.txt")
    solution = os.path.join(day, "solution.py")

    if not os.path.exists(data) or force_remake == "y":
        with open(data, "w+") as f:
            pass
    else:
        print(f"{ data } already exists")

    if not os.path.exists(solution) or force_remake == "y":
        with open(solution, "w+") as f:
            f.writelines(["with open(\"data.txt\") as f:\n",
                          "    pass\n"])
    else:
        print(f"{ solution } already exists")