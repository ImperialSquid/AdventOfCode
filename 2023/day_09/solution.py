with open("data.txt") as f:
    seqs = list()
    for line in f:
        seqs.append([int(num) for num in line.strip().split()])


def next_value(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq) - 1)]
    if all([diff == 0 for diff in diffs]):
        return seq[0]
    else:
        return seq[-1] + next_value(diffs)


def first_value(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq) - 1)]
    if all([diff == 0 for diff in diffs]):
        return seq[0]
    else:
        return seq[0] - first_value(diffs)


nexts = [next_value(seq) for seq in seqs]
firsts = [first_value(seq) for seq in seqs]

print("Solution 1: " + str(sum(nexts)))
print("Solution 2: " + str(sum(firsts)))
