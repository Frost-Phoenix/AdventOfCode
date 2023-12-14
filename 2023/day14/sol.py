# https://adventofcode.com/2023/day/14


def part_1(file: str) -> int:
    lines = list(map(list, open(file, 'r').readlines()))

    res = 0
    n = len(lines)
    n1 = len(lines[0])
    count = [0] * n

    for i in range(n-1, -1, -1):
        for j in range(n1):
            if lines[i][j] == "O":
                count[j] += 1
                lines[i][j] = "."
            elif lines[i][j] == "#":
                if count[j] > 0:
                    for k in range(i+1, i+1+count[j]):
                        lines[k][j] = "O"
                    count[j] = 0

    for j,nb in enumerate(count):
        for k in range(count[j]):
            lines[k][j] = "O"

    for i,l in enumerate(lines):
        res += (n - i) * l.count("O")

    return res

def main() -> None:
    # 106517
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")


if __name__  == "__main__":
    main()
