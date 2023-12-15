# https://adventofcode.com/2022/day/1


def part_1(file: str) -> int:
    return max([sum([int(nb) for nb in elve.split('\n')]) for elve in open(file, 'r').read().split('\n\n')])

def part_2(file: str) -> int:
    return sum(sorted([sum([int(nb) for nb in elve.split('\n')]) for elve in open(file, 'r').read().split('\n\n')], reverse=True)[:3])

def main() -> None:
    # 70296
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 205381
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()