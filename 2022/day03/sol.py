# https://adventofcode.com/2022/day/


def part_1(file: str) -> int:

    def get_repeat_char(l: str) -> str:
        for c in l[:len(l)//2]:
            if c in l[len(l)//2:]: return c

    lines = open(file, 'r').readlines()

    res = 0

    for l in lines:
        l = l[:-1]
        c = get_repeat_char(l)
        res += ord(c) - ord("a") + 1 if c.islower() else ord(c) - ord('A') + 1 + 26

    return res

def main() -> None:
    # 7581
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")


if __name__  == "__main__":
    main()
