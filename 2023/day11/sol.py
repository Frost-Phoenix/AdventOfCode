# https://adventofcode.com/2023/day/11


def solve(file: str, expantion: int) -> int:
    lines = open(file, 'r').readlines()
    
    # Get all dots rows and asign an unique id to each galaxie
    id = 0
    pos = {}
    line_to_add = []
    for r,l in enumerate(lines):
        l = list(l[:-1])
        all_dots = True
        for c,char in enumerate(l):
            if char != ".":
                all_dots = False
                l[c] = id
                pos[id] = (r,c)
                id += 1

        if all_dots: line_to_add.append(r)
        lines[r] = l
        
    # Get all dots colums
    col_to_add = []
    n = len(lines)
    for c in range(len(lines[0])-1):
        all_dots = True
        for r in range(n):
            if lines[r][c] != ".":
                all_dots = False
                break
        if all_dots: col_to_add.append(c)

    # Get pairs
    pairs = []
    for i in range(id):
        for j in range(i+1, id):
            pairs.append((i,j))

    # Get distances    
    res = 0
    for a,b in pairs:
        p1 = pos[a]
        p2 = pos[b]
        nb_steps = 0

        for i in [0,1]:
            if p1[i] - p2[i] > 0:
                r = range(p2[i], p1[i]+1)
                nb_steps += p1[i] - p2[i] + ((expantion - 1) * len(set(r).intersection(line_to_add if i == 0 else col_to_add)))
            else:
                r = range(p1[i], p2[i]+1)
                nb_steps += p2[i] - p1[i] + ((expantion - 1) * len(set(r).intersection(line_to_add if i == 0 else col_to_add)))

        res += nb_steps

    return res

def main():
    # 10077850
    part_1_sol = solve("input.txt", 2)
    print(f"part 1 sol: {part_1_sol}")

    # 504715068438
    part_2_sol = solve("input.txt", 1000000)
    print(f"part 2 sol: {part_2_sol}")
    

if __name__ == "__main__":
    main()