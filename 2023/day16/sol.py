# https://adventofcode.com/2023/day/16

from collections import deque as queue


def get_grid(file: str) -> list[list[str]]:
    grid = open(file, 'r').read().split('\n')

    for i,l in enumerate(grid):
        grid[i] = ["#"] + list(l) + ["#"]

    return [["#"] * len(grid[0])] + grid + [["#"] * len(grid[0])]

def part_1(file: str) -> int:
    grid = get_grid(file)

    directions = {
        "U": (1,0),
        "L": (0,-1),
        "D": (-1,0),
        "R": (0,1)
    }
    moves = {
        '-': (((0,1), "R"), ((0,-1), "L")),
        '|': (((1,0), "U"), ((-1,0), "D")),
        '/': {'L': ((1,0), "U"), 'R': ((-1,0), "D"), 'U': ((0,-1), "L"), 'D': ((0,1), "R")},
        chr(92): {'L': ((-1,0), "D"), 'R': ((1,0), "U"), 'U': ((0,1), "R"), 'D': ((0,-1), "L")},
    }

    pos_list = queue()
    pos_list.append(((1,1), 'R'))

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

def main() -> None:
    # 7788
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")


if __name__  == "__main__":
    main()