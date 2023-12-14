# https://adventofcode.com/2023/day/14


def roll(grid: list[list[str]], n: int) -> None:
    count = [0] * n

    for i in range(n-1, -1, -1):
        for j in range(n):
            if grid[i][j] == "O":
                count[j] += 1
                grid[i][j] = "."
            elif grid[i][j] == "#":
                if count[j] > 0:
                    for k in range(i+1, i+1+count[j]):
                        grid[k][j] = "O"
                    count[j] = 0

    for j,nb in enumerate(count):
        for k in range(count[j]):
            grid[k][j] = "O"

def rotate(grid: list[list[str]]) -> list[list[str]]:
    return [list(l) for l in list(zip(*grid[::-1]))]

def cycle(grid: list[list[str]], n: int) -> list[list[str]]:
    for i in range(4):
        roll(grid, n)
        grid = rotate(grid)
    return grid

def part_1(file: str) -> int:
    lines = list(map(list, open(file, 'r').readlines()))

    res = 0
    n = len(lines)

    roll(lines, n)

    for i,l in enumerate(lines):
        res += (n - i) * l.count("O")

    return res

def part_2(file: str) -> int:
    lines = list(map(list, [l[:-1] for l in open(file, 'r').readlines()]))

    res = 0
    n = len(lines)
    grid = lines

    i = 0
    past_grids = []
    while str(grid) not in past_grids:
        past_grids.append(str(grid))
        grid = cycle(grid, n)
        i += 1

    loop_len = past_grids.index(str(grid)) - i

    while (1000000000 - i) % loop_len != 0:
        grid = cycle(grid, n)
        i += 1

    for i,l in enumerate(grid):
        res += (n - i) * l.count("O")

    return res

def main() -> None:
    # 106517
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")

    # 79723
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()
