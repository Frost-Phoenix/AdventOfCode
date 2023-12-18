# https://adventofcode.com/2023/day/ 


def print_grid(grid: list[list[str]]) -> None:
    for l in grid:
        for c in l:
            print(c, end='')
        print()

def get_grid_size(moves: list[str]) -> int:
    x,y = 0,0
    pos = []

    for l in moves:
        l = l[:-1].split()
        d, nb = l[0], int(l[1])

        if d == 'U': y -= nb
        elif d == 'D': y += nb
        elif d == 'R': x += nb
        elif d == 'L': x -= nb

        pos.append((y,x))

    return max(pos)

def get_grid(moves: list[str]) -> list[list[str]]:
    nb_row, nb_col = get_grid_size(moves)

    return [['.' for __ in range(nb_col + 1)] for _ in range(nb_row + 1)]

def dig(grid: list[list[str]], x: int, y: int, d: int, nb: int) -> tuple[int,int]:
    for _ in range(nb):
        grid[y][x] = '#'

        if d == 'U': y -= 1
        elif d == 'D': y += 1
        elif d == 'R': x += 1
        elif d == 'L': x -= 1

    return (x,y)

def get_new_grid(grid: list[list[str]]) -> list[list[str]]:
    tmp = [['.' for __ in range(len(grid[0]) + 2)]]
    
    for i in range(len(grid)): grid[i] = ['.'] + grid[i] + ['.']

    return tmp + grid + tmp

def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0
    moves = []
    x,y = 0,0
    grid = get_grid(lines)

    for l in lines:
        l = l[:-1].split()
        d, nb = l[0], int(l[1])

        x,y = dig(grid, x, y, d, nb)

    grid = get_new_grid(grid)

    print_grid(grid)

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