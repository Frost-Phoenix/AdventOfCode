# https://adventofcode.com/2023/day/ 


def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0

    for l in lines:
        l = l[:-1]

    return res

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0

    for l in lines:
        l = l[:-1]

    return res

def main() -> None:
    # 
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()