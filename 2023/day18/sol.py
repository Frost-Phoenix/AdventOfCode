# https://adventofcode.com/2023/day/18

from collections import deque as queue


def print_grid(grid: list[list[str]]) -> None:
    for l in grid:
        for c in l:
            print(c, end='')
        print()

def get_min_max_pos(moves: list[str]) -> int:
    x,y = 0,0
    pos_x, pos_y = [0], [0]

    for l in moves:
        l = l[:-1].split()
        d, nb = l[0], int(l[1])

        if d == 'U': y -= nb
        elif d == 'D': y += nb
        elif d == 'R': x += nb
        elif d == 'L': x -= nb

        pos_x.append(x)
        pos_y.append(y)

    return ((min(pos_x),min(pos_y)), (max(pos_x),max(pos_y)))

def get_grid(moves: list[str], min_pos: tuple[int,int], max_pos: tuple[int,int]) -> list[list[str]]:
    return [['.' for __ in range(abs(min_pos[0]) + abs(max_pos[0]) + 1)] for _ in range(abs(min_pos[1]) + abs(max_pos[1]) + 1)]

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

def get_outer_cells_nb(grid: list[list[str]]) -> int:
    nb = 0    
    q = queue()
    q.append((0,0))

    visited = grid.copy()

    nb_row = len(grid)
    nb_col = len(grid[0])

    # BFS
    while q:
        x, y = q.popleft()

        if visited[y][x] not in "#$":
            visited[y][x] = '$'
            
            if x != 0 and x != nb_col - 1 and y != 0 and y != nb_row - 1:
                nb += 1

            for nx, ny in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0 <= x+nx < nb_col and 0 <= y+ny < nb_row:
                    if visited[y+ny][x+nx] not in "#$":
                        q.append((x+nx,y+ny))

    return nb_row * nb_col - sum([i.count('$') for i in visited])

def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()

    min_pos, max_pos = get_min_max_pos(lines)
    x,y = abs(min_pos[0]),abs(min_pos[1])
    grid = get_grid(lines, min_pos, max_pos)

    for l in lines:
        l = l[:-1].split()
        d, nb = l[0], int(l[1])

        x,y = dig(grid, x, y, d, nb)

    grid = get_new_grid(grid)

    return get_outer_cells_nb(grid)

def main() -> None:
    # 106459
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    

if __name__  == "__main__":
    main()