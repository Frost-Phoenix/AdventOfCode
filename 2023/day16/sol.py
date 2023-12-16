# https://adventofcode.com/2023/day/16

from collections import deque as queue


def get_grid(file: str) -> list[list[str]]:
    grid = open(file, 'r').read().split('\n')

    for i,l in enumerate(grid):
        grid[i] = ["#"] + list(l) + ["#"]

    return [["#"] * len(grid[0])] + grid + [["#"] * len(grid[0])]

def get_nb_tile_energized(grid: list[list[str]], start_pos: tuple[tuple[int,int], str]) -> int:
    directions = {
        "D": (1,0),
        "L": (0,-1),
        "U": (-1,0),
        "R": (0,1)
    }
    moves = {
        '-': (((0,1), "R"), ((0,-1), "L")),
        '|': (((1,0), "D"), ((-1,0), "U")),
        '/': {'L': ((1,0), "D"), 'R': ((-1,0), "U"), 'U': ((0,1), "R"), 'D': ((0,-1), "L")},
        chr(92): {'L': ((-1,0), "U"), 'R': ((1,0), "D"), 'U': ((0,-1), "L"), 'D': ((0,1), "R")},
    }

    pos_list = queue()
    pos_list.append(start_pos)

    nb_row = len(grid)
    nb_col = len(grid[0])
    visited = [[False for c in range(nb_col)] for r in range(nb_row)]
    nb_energized = 0
    while len(pos_list) != 0:
        current_pos, d = pos_list.popleft()
        c = grid[current_pos[0]][current_pos[1]]
        
        if c != "#" and not visited[current_pos[0]][current_pos[1]]: 
            nb_energized += 1
            visited[current_pos[0]][current_pos[1]] = True

        if c == "#": continue
        
        if c == ".": mv = [(directions[d], d)]
        elif c == "|" or c == "-": mv = moves[c]
        else: mv = [moves[c][d]]
        
        for delta, new_dir in mv:
            new_pos_x = current_pos[0] + delta[0] 
            new_pos_y = current_pos[1] + delta[1]
            new_pos_c = grid[new_pos_x][new_pos_y]
            new_pos = (new_pos_x, new_pos_y)

            if (new_pos_c == "|" or new_pos_c == "-") and visited[new_pos_x][new_pos_y]: continue

            pos_list.append((new_pos, new_dir))

    return nb_energized

def part_1(file: str) -> int:
    grid = get_grid(file)

    return get_nb_tile_energized(grid, ((1,1), "R"))

def part_2(file: str) -> int:
    grid = get_grid(file)

    nb_row = len(grid)
    nb_col = len(grid[0])

    top_row    = max([get_nb_tile_energized(grid, ((1,x), "D"))          for x in range(1, nb_col - 1)])
    bottom_row = max([get_nb_tile_energized(grid, ((nb_row - 2,x), "U")) for x in range(1, nb_col - 1)])
    left_col   = max([get_nb_tile_energized(grid, ((x,1), "D"))          for x in range(1, nb_row - 1)])
    right_col  = max([get_nb_tile_energized(grid, ((x,nb_col - 2), "U")) for x in range(1, nb_row - 1)])

    return max([top_row, bottom_row, left_col, right_col])

def main() -> None:
    # 7788
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 7987
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()