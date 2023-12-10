# https://adventofcode.com/2023/day/ 


path_map = {
    "S": [(-1,0),(0,-1),(0,1),(1,0)],
    "─": [(0,-1),(0, 1)], 
    "│": [(-1,0),(1, 0)], 
    "╭": [(1,0),(0, 1)],
    "╮": [(0,-1),(1, 0)], 
    "╯": [(0,-1),(-1, 0)],
    "╰": [(-1,0),(0, 1)]
}

def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()

    start_pos = None
    for r,l in enumerate(lines):
        l = l[:-1]
        lines[r] = " " + l + " "
        
        c = l.find("S")
        if c != -1: start_pos = (r+1,c+1)

    len_line_0 = len(lines[0])
    lines = [len_line_0 * " "] + lines + [len_line_0 * " "]

    for r,c in [(-1,0),(0,1),(1,0),(0,-1)]:
        if lines[start_pos[0] + r][start_pos[1] + c] != " " and (-r,-c) in path_map[lines[start_pos[0] + r][start_pos[1] + c]]:

            current_pos = (start_pos[0] + r, start_pos[1] + c)
            nb_steps = 0
            visited = []
            
            can_move = True
            while can_move and lines[current_pos[0]][current_pos[1]] != "S":
                can_move = False
                current_tile = lines[current_pos[0]][current_pos[1]]
            
                for r,c in path_map[current_tile]:
                    new_pos = (current_pos[0] + r, current_pos[1] + c)
                    tile = lines[new_pos[0]][new_pos[1]]
            
                    if tile != " " and new_pos not in visited:
                        if tile != "S" or tile == "S" and visited != []:
                            if (r,c) in path_map[current_tile] and (-r,-c) in path_map[tile]: 
                                visited.append(current_pos)
                                current_pos = new_pos
                                nb_steps += 1
                                can_move = True
                                break

            if can_move: return (nb_steps + 1) // 2

    return -1

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()

    start_pos = None
    for r,l in enumerate(lines):
        l = l[:-1]
        lines[r] = " " + l + " "
        
        c = l.find("S")
        if c != -1: start_pos = (r+1,c+1)

    len_line = len(lines)
    len_line_0 = len(lines[0])
    lines = [len_line_0 * " "] + lines + [len_line_0 * " "]
    new_grid = []

    for r,c in [(-1,0),(0,1),(1,0),(0,-1)]:
        new_grid = [[0] * len_line_0 for i in range(len(lines))] 
        if lines[start_pos[0] + r][start_pos[1] + c] != " " and (-r,-c) in path_map[lines[start_pos[0] + r][start_pos[1] + c]]:

            current_pos = (start_pos[0] + r, start_pos[1] + c)
            visited = []
            
            new_grid[current_pos[0]][current_pos[1]] = lines[start_pos[0] + r][start_pos[1] + c]

            can_move = True
            while can_move and lines[current_pos[0]][current_pos[1]] != "S":
                can_move = False
                current_tile = lines[current_pos[0]][current_pos[1]]
            
                for r,c in path_map[current_tile]:
                    new_pos = (current_pos[0] + r, current_pos[1] + c)
                    tile = lines[new_pos[0]][new_pos[1]]
            
                    if tile != " " and new_pos not in visited:
                        if tile != "S" or tile == "S" and visited != []:
                            if (r,c) in path_map[current_tile] and (-r,-c) in path_map[tile]: 
                                visited.append(current_pos)
                                current_pos = new_pos
                                new_grid[current_pos[0]][current_pos[1]] = tile
                                can_move = True
                                break

            if can_move: break

    for i,l in enumerate(new_grid):
        tmp = []
        for e in l:
            tmp.append(e)
            if e == "─" or e == "╭" or e == "╰" or e == "S": tmp.append("─")
            else: tmp.append(" ")
        new_grid[i] = tmp
    tmp_grid = []
    for l in new_grid:
        tmp = [" "] * len(l)
        for i,e in enumerate(l):
            if e == "│" or e == "╭" or e == "╮" or e == "S": tmp[i] = "│"
        tmp_grid.append(l)
        tmp_grid.append(tmp)

    new_grid = tmp_grid
    visited = []
    to_explore = [(0,0)]

    len_new_grid = len(new_grid)
    len_new_grid_0 = len(new_grid[0])

    while len(to_explore) != 0:
        current = to_explore.pop()
        for r,c in [(-1,0),(0,1),(1,0),(0,-1)]:
            new_pos = (current[0]+r,current[1]+c)
            if new_pos not in visited:
                if new_pos[0] >= 0 and new_pos[0] < len_new_grid and new_pos[1] >= 0 and new_pos[1] < len_new_grid_0:
                    if new_grid[new_pos[0]][new_pos[1]] == " " or new_grid[new_pos[0]][new_pos[1]] == 0:
                        to_explore.append(new_pos)

            if current[0] % 2 == 0 and current[1] % 2 == 0:
                if new_grid[current[0]][current[1]] == 0:
                    new_grid[current[0]][current[1]] = " "

            visited.append(current)

    res = 0
    for l in new_grid:
       for e in l:
            if e == 0: 
                res += 1
    
    return res

def main() -> None:
    # 6886
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 371
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()