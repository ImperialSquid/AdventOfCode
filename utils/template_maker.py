import os

year = input("AoC Year: ")

dirs = ([os.path.join("..", year), ] +
        [os.path.join("..", year, "day_"+str(day+1).zfill(2)) for day in range(25)])

for dir in dirs:
    if not os.path.exists(dir):
        os.mkdir(dir)

for day in dirs[1:]:
    with open(os.path.join(day, "data.txt"), "w+") as f:
        pass

    with open(os.path.join(day, "solution.py"), "w+") as f:
        f.writelines(["with open(\"data.txt\") as f:\n",
                      "    pass\n"])
