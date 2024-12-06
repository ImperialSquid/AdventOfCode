from functools import cmp_to_key

def get_data(file):
    page_orders = []
    page_updates = []

    with open(file) as f:
        line = f.readline().strip()

        while line != "":
            page_orders.append(line.strip().split("|"))
            line = f.readline().strip()

        line = f.readline()
        while line != "":
            page_updates.append(line.strip().split(","))
            line = f.readline().strip()

    return page_orders, page_updates

def solve_part1_1(orders, updates):
    # if XX|YY is in page orders
    #   page_order_dict[(XX, YY)] = -1 (correct order)
    #   page_order_dict[(YY, XX)] = 1 (incorrect order)
    # use get with default 0 for no change
    #
    # using a dict also gives constant time comparisons compared to searching
    # the page order list every time
    page_order_dict = dict([((p_o[0], p_o[1]), -1) for p_o in orders])
    page_order_dict.update(dict(((p_o[1], p_o[0]), 1) for p_o in orders))

    def page_order_compare(a, b):
        return page_order_dict.get((a, b), 0)
    page_order_key = cmp_to_key(page_order_compare)

    p1_total = 0
    p2_total = 0

    for page in updates:
        sorted_page = sorted(page, key=page_order_key)

        # print(page)
        # print(sorted_page)
        # quit()

        if all(x == y for x, y in zip(page, sorted_page)):
            p1_total += int(page[len(page) // 2])
        else:
            p2_total += int(sorted_page[len(page) // 2])

    return p1_total, p2_total

def main():
    orders, updates = get_data("data.txt")

    p1, p2 = solve_part1_1(orders, updates)

    print(f"Part 1 Solution: { p1 }")
    print(f"Part 2 Solution: { p2 }")

if __name__ == '__main__':
    main()
