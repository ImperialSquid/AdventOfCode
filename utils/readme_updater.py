def update_readme(year: str):
    with open("../README.md", "a") as readme:
        readme.write(f"\n\n## { year }\n\n")

        readme.write("<details><summary>Python 00/50</summary>\n\n")

        readme.write("| Day                             | Part 1             | Part 2             |\n")
        readme.write("|---------------------------------|--------------------|--------------------|\n")

        for day in range(25):
            num = str(day+1).zfill(2)
            readme.write(f"| [{ num }](./{ year }/day_{ num }/solution.py) | :x:                | :x:                |\n")

        readme.write("\n</details>")

if __name__ == "__main__":
    year = input("AoC Year: ")

    update_readme(year)