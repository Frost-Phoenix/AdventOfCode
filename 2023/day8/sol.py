# https://adventofcode.com/2023/day/8

from math import lcm


def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    
    res = 0
    steps = {}
    patern = lines[0][:-1]

    for l in lines[2:]:
        l = l[:-1]
        key, val = l.split(" = ")
        val = val[1:-1].split(", ")

        steps[key] = val

    done = False
    current_step = "AAA"
    current_action = 0
    while not done:
        res += 1

        current_step = steps[current_step]
        next = current_step[0] if patern[current_action % len(patern)] == 'L' else current_step[1]
        current_step = next

        if (next == "ZZZ"): done = True

        current_action += 1

    return res

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()
    
    steps = {}
    patern = lines[0][:-1]
    current_steps = []

    for l in lines[2:]:
        l = l[:-1]
        key, val = l.split(" = ")
        val = val[1:-1].split(", ")

        steps[key] = val
        if key[-1] == 'A': current_steps.append(key)


    res = 1
    for step in current_steps:
        current_step = step
        current_action = 0
        nb_steps = 0
        done = False
        while not done:
            nb_steps += 1

            current_step = steps[current_step]
            next = current_step[0] if patern[current_action % len(patern)] == 'L' else current_step[1]
            current_step = next
    
            if (next[-1] == 'Z'): done = True

            current_action += 1

        res = lcm(res, nb_steps)

    return res

def main():
    # 14257
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 16187743689077
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()