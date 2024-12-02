from aocd import get_data
import os

with open("../secrets", "r") as secrets:
    os.environ["AOC_SESSION"] = secrets.read().strip()

year = input("AoC Year: ")
day = input("AoC Day: ")

with open(f"../{ year }/day_{ str(int(day)).zfill(2) }/data.txt", "w") as file:
    data = get_data(day=int(day), year=int(year))
    file.writelines(data)