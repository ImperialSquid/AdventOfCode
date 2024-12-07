import time

start = time.time()

equations = []

with open("data.txt") as f:
    for line in f:
        lhs, rhs = line.strip().split(": ")
        rhs = [int(v) for v in rhs.split(" ")]
        equations.append((int(lhs), rhs))

def evaluate_equations(target, stack, ops, layer = 0):
    if len(stack) == 1:
        # print("bottom", target, stack[0], layer)
        return target == stack[0]
    if stack[-1] > target:
        # all operations are "additive" (their result will be bigger than both inputs)
        # so if we're over the total we can exit early
        return False
    # print(target, stack, x, y, layer)

    x, y = stack[-2:]
    stacks = []
    for op in ops:
        stacks.append(stack[:-2] + [op(x, y), ])

    return any(evaluate_equations(target, s, ops, layer + 1) for s in stacks)

operators = [lambda x, y: x + y,
             lambda x, y: x * y,
             lambda x, y: int(str(y) + str(x))]  # our stack is reverse so it's y || x not x || y

p1_total = 0
p2_total = 0

for eq_i, eq in enumerate(equations):
    # print(eq_i)
    rhs = list(reversed(eq[1]))
    # print(eq)
    # print(evaluate_equations(eq[0], rhs))
    if evaluate_equations(eq[0], rhs, operators[:2]):
        p1_total += eq[0]
    if evaluate_equations(eq[0], rhs, operators):
        p2_total += eq[0]

end = time.time()

print(f"Part 1 Solution: { p1_total }")
print(f"Part 2 Solution: { p2_total }")
print(f"Total Time: {end - start}")
