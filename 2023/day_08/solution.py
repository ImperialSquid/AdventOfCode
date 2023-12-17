# I DO NOT like this puzzle, the assumption that the ghost cycles synch up on the
# lcm of the lengths is very non-obvious to me, feels like far too much baked in assumptions wie

from math import lcm

with open("data.txt") as f:
    instructions = f.readline().strip().replace("L", "0").replace("R", "1")
    instructions = [int(inst) for inst in instructions]

    f.readline()

    nodes = dict()
    for line in f:
        line = line.replace("(", "").replace(")", "").replace(" ", "").strip()

        splits = line.split("=")
        start = splits[0]
        opts = splits[1].split(",")

        nodes[start] = opts

ghost_pos = [pos for pos in nodes if pos[-1] == "A"]
ghost_loops = list()

for pos in ghost_pos:
    steps = 0

    while pos[-1] != "Z":  # find first visit to Z node
        opts = nodes[pos]
        pos = opts[instructions[steps % len(instructions)]]
        steps += 1
    ghost_loops.append(steps)


print("Solution 1: " + str(ghost_loops[0]))
print("Solution 2: " + str(lcm(*ghost_loops)))
