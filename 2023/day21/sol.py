# https://adventofcode.com/2023/day/21


def get_grid(file: str):
    grid = [list(row) for row in open(file, 'r').read().split('\n')]

    for i in range(len(grid)):
        grid[i] = ['#'] + grid[i] + ['#']

    tmp = ['#' for i in range(len(grid[0]))]

    return [tmp] + grid + [tmp]

def get_start_pos(grid, nb_row: int, nb_col: int):
    for r in range(nb_row):
        for c in range(nb_col):
            if grid[r][c] == 'S':
                grid[r][c] = '.'
                return (r, c)

def get_next_pos(grid, pos):
    return [(pos[0] + n_row, pos[1] + n_col) for n_row, n_col in [(0,1) , (0,-1) , (1,0) , (-1,0)] if grid[pos[0] + n_row][pos[1] + n_col] != '#']

def find_next_pos(grid, start, nb_steps: int) -> int:
    pos_list = [start]

    while nb_steps > 0:
        tmp = []
        for pos in pos_list:
            for new_pos in get_next_pos(grid, pos):
                if new_pos not in tmp:
                    tmp.append(new_pos)
        pos_list = tmp

        nb_steps -= 1

    return len(pos_list)

def part_1(file: str) -> int:
    grid = get_grid(file)

    nb_row = len(grid)
    nb_col = len(grid[0])

    start = get_start_pos(grid, nb_row, nb_col)

    return find_next_pos(grid, start, 64)

def main() -> None:
    # 3637
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")


if __name__  == "__main__":
    main()