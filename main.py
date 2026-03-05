def is_safe(levels):
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]

    increasing = all(d > 0 for d in diffs)
    decreasing = all(d < 0 for d in diffs)

    if not (increasing or decreasing):
        return False

    return all(1 <= abs(d) <= 3 for d in diffs)


def is_safe_with_remove(levels):

    if is_safe(levels):
        return True

    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True

    return False


part1 = 0
part2 = 0

with open("file.txt") as f:
    for line in f:
        levels = list(map(int, line.split()))

        if is_safe(levels):
            part1 += 1

        if is_safe_with_remove(levels):
            part2 += 1


print("Part 1:", part1)
print("Part 2:", part2)