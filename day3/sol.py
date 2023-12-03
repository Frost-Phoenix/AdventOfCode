# https://adventofcode.com/2023/day/3


def get_grid(file: str) -> list[str]:
    grid = open(file).read().splitlines()
    line_len = len(grid[0])

    for i in range(len(grid)):
        grid[i] = "." + grid[i] + "."
    grid = ["." * line_len] + grid + ["." * line_len]

    return grid

def get_symbols_pos(file: list[str]) -> list[tuple[int,int]]:
    res = []
    
    for r,l in enumerate(file):
        for c,char in enumerate(l):
            if (char != '.' and not char.isdigit()):
                res.append((r,c))

    return res

def check_symbols(symbols_pos: list[tuple[int,int]], line: int, start: int, end: int) -> bool:
    for i in range(start-1, end+2):
        for offset in [-1, 0, 1]:
            if (line + offset, i) in symbols_pos:
                return True

    return False   

def part_1(file: str) -> int:
    grid = get_grid(file)

    sum = 0
    nb_start = None
    symbols_pos = get_symbols_pos(grid)

    for r, l in enumerate(grid):
        current_nb = ""

        for c,char in enumerate(l):

            if char.isdigit():
                if nb_start == None: 
                    nb_start = c
                current_nb += char

            elif nb_start != None: 
                if check_symbols(symbols_pos, r, nb_start, c - 1): 
                    sum += int(current_nb)
                current_nb = ""
                nb_start = None

    return sum

def main():
    # 533775
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")

    # part_2_sol = part_2("input.txt")
    # print(f"part 2 sol: {part_2_sol}")


if __name__ == "__main__":
    main()