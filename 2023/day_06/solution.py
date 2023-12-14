from math import floor, ceil

with open("data.txt") as f:
    data = f.readline().split(":")[1]
    times = [int(num) for num in data.split()]
    big_time = int(data.replace(" ", ""))

    data = f.readline().split(":")[1]
    dists = [int(num) for num in data.split()]
    big_dist = int(data.replace(" ", ""))

total = 1
a = 1
for i in range(len(times)):
    b = -1 * times[i]
    c = dists[i]

    # solve quadratic to find bet voudaries for yime to press button
    # revord < d = pressed * (total - pressed)
    # pressed ** 2 - pressed * total + record < 0
    # 1e-6 acts as fudge for inequality
    lower = ceil((-1 * b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) + 1e-6)
    upper = floor((-1 * b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) - 1e-6)

    total *= (upper - lower + 1)


b = -1 * big_time
c = big_dist
lower = ceil((-1 * b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) + 1e-6)
upper = floor((-1 * b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) - 1e-6)

print("Solition 1: " + str(total))
print("Solution 2: " + str(upper - lower + 1))