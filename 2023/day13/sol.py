# https://adventofcode.com/2023/day/ 


def part_1(file: str) -> int:

    def check_horizontal_sym(grid: list[str]) -> None | int:
        n = len(grid)
        for i in range(n - 1):
            if grid[i] == grid[i + 1]:
                t = i+1 >= n // 2
                r = range(i+1, n) if t else range(i-1, -1, -1)
                for j in r:
                    if grid[j] != grid[i-(j-i)+1 if t else i+(i-j)+1]:
                        break
                else: return i + 1

        return None

    def check_vertical_sym(grid: list[str]) -> None | int:
        def check_col(c1, c2, nb_row) -> bool:
            for r in range(nb_row):
                if grid[r][c1] != grid[r][c2]: return False
            else: return True

        nb_col = len(grid[0])
        nb_row = len(grid)

        for c in range(nb_col-1):
            if check_col(c, c+1, nb_row):
                t = c+1 >= nb_col // 2
                r = range(c+2, nb_col) if t else range(c-1, -1, -1)
                for c2 in r:
                    if not check_col(c2, c-(c2-c)+1 if t else c+(c-c2)+1, nb_row): break
                else: return c + 1

        return None
    
    lines = open(file, 'r').readlines()

    res = 0
    girds = []

    tmp = []
    for l in lines:
        l = l[:-1]
        if l != "": tmp.append(l)
        else: 
            girds.append(tmp)
            tmp = []
    
    girds.append(tmp)

    tmp = []
    for i,g in enumerate(girds):
        horizontal_sym = check_horizontal_sym(g)
        if horizontal_sym != None:
            tmp.append((i,horizontal_sym * 100))
            res += horizontal_sym * 100
        else:
            vertical_sym = check_vertical_sym(g)
            tmp.append((i,vertical_sym))
            res += vertical_sym

    print(res)
    return tmp

def part_2(file: str) -> int:

    def check_horizontal_sym(grid: list[str]) -> None | int:
        def check_fix(grid: list[str], r1, r2) -> bool:
            l1 = grid[r1]
            l2 = grid[r2]
            has_change = False
            for k in range(len(l1)):
                if l1[k] != l2[k]:
                    if not has_change: has_change = True
                    else: return False
            return True
        
        n = len(grid)
        fix = False
        for i in range(n - 1):
            if grid[i] != grid[i + 1]: fix = check_fix(grid, i, i+1)
            if grid[i] == grid[i + 1] or fix:
                t = i+1 >= n // 2
                r = range(i+1, n) if t else range(i-1, -1, -1)
                for j in r:
                    j2 = i-(j-i)+1 if t else i+(i-j)+1
                    if grid[j] != grid[j2]:
                        if fix: break
                        if check_fix(grid, j, j2): fix = True
                        else: break
                else: return i + 1

        return None

    def check_vertical_sym(grid: list[str]) -> None | int:
        def check_col(c1, c2, nb_row) -> bool:
            for r in range(nb_row):
                if grid[r][c1] != grid[r][c2]: return False
            else: return True

        def check_fix(c1, c2, nb_row) -> bool:
            has_change = False
            for r in range(nb_row):
                if grid[r][c1] != grid[r][c2]: 
                    if not has_change: has_change = True
                    else: return False
            return True

        nb_col = len(grid[0])
        nb_row = len(grid)

        fix = False
        for c in range(nb_col-1):
            valid_cols = check_col(c, c+1, nb_row)
            if not valid_cols: fix = check_fix(c, c+1, nb_row)
            if valid_cols or fix:
                t = c+1 >= nb_col // 2
                r = range(c+2, nb_col) if t else range(c-1, -1, -1)
                for c2 in r:
                    if not check_col(c2, c-(c2-c)+1 if t else c+(c-c2)+1, nb_row): 
                        if fix: break
                        if check_fix(c2, c-(c2-c)+1 if t else c+(c-c2)+1, nb_row): fix = True
                        else: break
                else: return c + 1

        return None

    lines = open(file, 'r').readlines()

    res = 0
    girds = []

    tmp = []
    for l in lines:
        l = l[:-1]
        if l != "": tmp.append(l)
        else: 
            girds.append(tmp)
            tmp = []
    
    girds.append(tmp)

    tmp = []
    for i,g in enumerate(girds):
        horizontal_sym = check_horizontal_sym(g)
        if horizontal_sym != None:
            tmp.append((i,horizontal_sym * 100))
            res += horizontal_sym * 100
        else:
            vertical_sym = check_vertical_sym(g)
            tmp.append((i,vertical_sym))
            res += vertical_sym

    print(res)
    return tmp

def main() -> None:
    # 30487
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")

    for i in range(len(part_1_sol)):
        if part_1_sol[i] < part_2_sol[i]:
            print(part_1_sol[i], "\t", part_2_sol[i])


if __name__  == "__main__":
    main()