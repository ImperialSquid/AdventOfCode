from aocd import get_data
import os

from aocd.exceptions import PuzzleLockedError

def get_aoc_data(year: str, days_input: str):
    with open("../secrets", "r") as secrets:
        os.environ["AOC_SESSION"] = secrets.read().strip()

    if days_input == "":
        days = [i + 1 for i in range(25)]
    elif "-" in days_input:
        start, end = days_input.split("-")
        days = [i for i in range(int(start), int(end) + 1)]
    else:
        days = [int(days_input), ]

    for day in days:
        with open(f"../{ year }/day_{ str(day).zfill(2) }/data.txt", "w") as file:
            try:
                data = get_data(day=int(day), year=int(year))
                file.writelines(data)
                print(f"Wrote { year }/{ str(day).zfill(2) } successfully!")
            except PuzzleLockedError:
                print(f"Input for { year }/{str(day).zfill(2)} not available yet...")
                break
            except Exception as e:
                print(f"Ran into other error on { year }/{ str(day).zfill(2) }...")
                print(e)

if __name__ == "__main__":
    year = input("AoC Year: ")
    days_input = input("AoC Day (XX for one day, XX-YY for multiple days, nothing for all days): ")
    
    get_aoc_data(year, days_input)