# https://adventofcode.com/2023/day/11


def part_1(file: str):
    lines = open(file, 'r').readlines()
    
    n1 = len(lines[0])-1
    line_to_add = []
    
    for r,l in enumerate(lines):
        l = list(l[:-1])
        all_dots = True
        for c,char in enumerate(l):
            if char != ".":
                all_dots = False
                
        if all_dots: line_to_add.append(r)
        lines[r] = list(l)
        
    offset = 0
    for i in line_to_add:
        del lines[i+offset]
        lines[i+offset:1] = [["."] * n1 for _ in range(2)]
        offset += 1

    col_to_add = []
    n0 = len(lines)
    for c in range(n1):
        all_dots = True
        for r in range(n0):
            if lines[r][c] != ".":
                all_dots = False
                break
        if all_dots: col_to_add.append(c)

    if (len(col_to_add) > 0):
        for r in range(n0):
            offset = 0
            for v in col_to_add:
                lines[r].insert(v+offset, ".")
                offset += 1
    
    id = 0
    pos = {}
    for r,l in enumerate(lines):
        for c,char in enumerate(l):
            if char == "#":
                l[c] = id
                pos[id] = (r,c)
                id += 1
        lines[r] = l

    pairs = []
    for i in range(id):
        for j in range(i+1, id):
            pairs.append((i,j))
    
    res = 0
    for a,b in pairs:
        p1 = pos[a]
        p2 = pos[b]
        nb_steps = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        res += nb_steps
    
    return res

def main():
    # 10077850
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")
    

if __name__ == "__main__":
    main()