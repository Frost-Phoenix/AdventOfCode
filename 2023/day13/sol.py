# https://adventofcode.com/2023/day/ 


def check_horizontal_sym(grid: list[str]) -> None | int:
    n = len(grid)
    for i in range(n - 1):
        if grid[i] == grid[i + 1]:
            if i+1 >= n //2:
                for j in range(i+1, n):
                    if grid[j] != grid[i-(j-i)+1]:
                        break
                else: return i + 1
            else: 
                for j in range(i-1, -1, -1):
                    if grid[j] != grid[i+(i-j)+1]:
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
            if c+1 >= nb_col // 2:
                for c2 in range(c+2, nb_col):
                    if not check_col(c2, c-(c2-c)+1, nb_row): break
                else: return c + 1
            else:
                for c2 in range(c-1, -1, -1):
                    if not check_col(c2, c+(c-c2)+1, nb_row): break
                else: return c + 1

    return None

def part_1(file: str) -> int:
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

    for i,g in enumerate(girds):
        horizontal_sym = check_horizontal_sym(g)
        if horizontal_sym != None:
            res += horizontal_sym * 100
        else:
            vertical_sym = check_vertical_sym(g)
            res += vertical_sym

    return res

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0

    for l in lines:
        l = l[:-1]

    return res

def main() -> None:
    # 
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()