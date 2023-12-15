# https://adventofcode.com/2023/day/ 


def part_1(file: str) -> int:
    lines = open(file, 'r').readline()

    res = 0
    for l in lines.split(","):
        tmp = 0
        for c in l:
            tmp += ord(c)
            tmp *= 17
            tmp %= 256

        res += tmp

    return res

def main() -> None:
    # 521341
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    

if __name__  == "__main__":
    main()