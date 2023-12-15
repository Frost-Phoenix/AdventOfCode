# https://adventofcode.com/2022/day/


def get_char_value(char: str) -> int:
    return ord(char) - ord("a") + 1 if char.islower() else ord(char) - ord('A') + 1 + 26

def get_repeat_char(l: str) -> str:
    for c in l[:len(l)//2]:
        if c in l[len(l)//2:]: return c

def part_1(file: str) -> int:
    return sum([get_char_value(get_repeat_char(l[:-1])) for l in open(file, 'r').readlines()])

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0

    for i in range(0, len(lines), 3):
        for c in lines[i][:-1]:
            if c in lines[i+1] and c in lines[i+2]:
                res += get_char_value(c)
                break

    return res

def main() -> None:
    # 7581
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")

    # 2525
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()
