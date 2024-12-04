from input_data_getter import get_aoc_data
from readme_updater import update_readme
from template_maker import setup_files

if __name__ == '__main__':
    setup_what = input("What to setup?\n"
                       "  f - Setup files\n"
                       "  d - Get data\n"
                       "  r - Update readme\n"
                       ": ")

    if "f" in setup_what or "d" in setup_what or "r" in setup_what:
        year = input("All - AoC Year: ")

        if "f" in setup_what:
            force_remake = input("Files - Force remake? (y/n): ")
            setup_files(year, force_remake)
            print("Files setup complete.")

        if "d" in setup_what:
            days = input("Data - AoC Days"
                         "  (XX for one day, XX-YY for multiple days, nothing for all days"
                         ": ")
            get_aoc_data(year, days)
            print("Data setup complete.")

        if "r" in setup_what:
            update_readme(year)
            print("README updated complete.")

    else:
        print("Invalid input")
