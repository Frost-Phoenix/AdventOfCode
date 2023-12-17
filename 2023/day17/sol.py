# https://adventofcode.com/2023/day/17

from heapq import heappush, heappop


def solve(file: str, part: int, max_strait: int):
    grid = [list(map(int, l.strip())) for l in open(file, 'r').readlines()]

    nb_row = len(grid)
    nb_col = len(grid[0])

    # heat_los, (row,col), (dir_row,dir_col), nb_steps_in_dir
    p_queue = [(0, (0,0), (0,0), 0)]

    seen = set()

    while p_queue:
        heat_los, (row,col), (dir_row,dir_col), nb_steps_in_dir = heappop(p_queue)

        if part == 1 and row == nb_row - 1 and col == nb_col - 1: return heat_los
        elif part == 2 and row == nb_row - 1 and col == nb_col - 1 and nb_steps_in_dir >= 4: return heat_los

        if ((row, col), (dir_row, dir_col), nb_steps_in_dir) in seen:
            continue

        seen.add(((row, col), (dir_row, dir_col), nb_steps_in_dir))

        if nb_steps_in_dir < max_strait and (dir_row, dir_col) != (0,0):
            new_row = row + dir_row
            new_col = col + dir_col
            if 0 <= new_row < nb_row and 0 <= new_col < nb_col:
                heappush(p_queue, (heat_los + grid[new_row][new_col], (new_row, new_col), (dir_row, dir_col), nb_steps_in_dir + 1))
            
        if part == 1 or nb_steps_in_dir >= 4 or (dir_row, dir_col) == (0,0):        
            for new_dir_row, new_dir_col in [(0,1), (0,-1), (1,0), (-1,0)]:
                if (new_dir_row, new_dir_col) != (dir_row,dir_col) and (new_dir_row, new_dir_col) != (-dir_row,-dir_col):
                    new_row = row + new_dir_row
                    new_col = col + new_dir_col
                    if 0 <= new_row < nb_row and 0 <= new_col < nb_col:
                        heappush(p_queue, (heat_los + grid[new_row][new_col], (new_row, new_col), (new_dir_row, new_dir_col), 1))
                    
    return -1

def main() -> None:
    # 1195
    part_1_sol = solve("input.txt", 1, 3)
    print(f"sol part 1: {part_1_sol}")
    
    # 1347
    part_2_sol = solve("input.txt", 2, 10)
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()