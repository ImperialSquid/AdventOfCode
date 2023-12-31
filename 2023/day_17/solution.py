from heapq import heappop, heappush

with open("data.txt") as f:
    grid = [[int(t) for t in row] for row in f.read().splitlines()]

grid_w = len(grid)

start = (0, 0)
dest = (grid_w - 1, grid_w - 1)

compass = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# sliiiiightly more efficient than manhatten dist, found by manually adjusting down power until consistency
step_cost = sum([t for row in grid for t in row]) ** (1/32)


def solve(min_steps, max_steps):
    visited = set()
    queue = []

    # states are (a star heuristic, running heat loss, (row, col), ((row_dir, col_dir), steps_dir))
    heappush(queue, (grid[0][1] + (grid_w*2-1)*step_cost, grid[0][1], (0, 1), ((0, 1), 1)))
    heappush(queue, (grid[1][0] + (grid_w*2-1)*step_cost, grid[1][0], (1, 0), ((1, 0), 1)))

    # print(queue)

    while queue:
        (heur, heat, (r, c), ((rd, cd), s)) = heappop(queue)

        if (r, c) == dest:
            return heat

        if ((r, c), ((rd, cd), s)) in visited:
            continue
        else:
            visited.add(((r, c), ((rd, cd), s)))

        # print("Curr: ", (heur, heat, (r, c), ((rd, cd), s)))

        if s < max_steps:  # only add forward if within max distance range
            new_r = r + rd
            new_c = c + cd

            if -1 < new_r < len(grid) and -1 < new_c < len(grid[0]):
                forward = (heat + grid[new_r][new_c] + (grid_w*2 - new_r - new_c)*step_cost,  # heuristic
                           heat + grid[new_r][new_c],  # actual heat (technically redundant but saves fiddling))
                           (new_r, new_c),  # position
                           ((rd, cd), s + 1))  # direction and steps
                # print("Forward: ", forward)
                heappush(queue, forward)

        if s >= min_steps:
            for comp_r, comp_c in compass:
                if (comp_r, comp_c) != (rd, cd) and (comp_r, comp_c) != (-rd, -cd):  # always add only left/right moves
                    new_r = r + comp_r
                    new_c = c + comp_c

                    if -1 < new_r < len(grid) and -1 < new_c < len(grid[0]):
                        new = (heat + grid[new_r][new_c] + (grid_w*2 - new_r - new_c)*step_cost,
                               heat + grid[new_r][new_c],
                               (new_r, new_c),
                               ((comp_r, comp_c), 1))
                        # print("LR: ", new)
                        heappush(queue, new)

        # print("Queue:", queue)
        # input()


print("Solution 1:", solve(0, 3))
print("Solution 2:", solve(4, 10))
