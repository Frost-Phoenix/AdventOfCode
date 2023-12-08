# https://adventofcode.com/2023/day/8


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

def main():
    # 14257
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")


if __name__  == "__main__":
    main()