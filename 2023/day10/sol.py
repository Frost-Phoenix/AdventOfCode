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

    lines = [len(lines[0]) * " "] + lines + [len(lines[0]) * " "]

    for r,c in [(-1,0),(0,1),(1,0),(0,-1)]:
        if lines[start_pos[0] + r][start_pos[1] + c] != " ":

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

    res = 0

    for l in lines:
        l = l[:-1]

    return res

def main() -> None:
    # 6886
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()