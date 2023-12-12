# https://adventofcode.com/2023/day/12

import itertools 

def bruteforce(charset: str, length: int) -> list[list[str]]:
    return [list(combination) for combination in itertools.product(charset, repeat=length)]

def get_unknow_len(springs: list[str], start: int) -> int:
    res = 0
    for c in springs[start:]:
        if c == "?": res += 1
        else: break
    
    return res
    
def is_valid(p: list[str], groups: list[int]) -> bool:
    groups_len = []
    current_len = 0
    last_c = None
    for c in p:
        if c == "#": 
            current_len += 1
            last_c = c
        elif last_c == "#":
            last_c = None
            groups_len.append(current_len)
            current_len = 0
    if current_len > 0: groups_len.append(current_len)
    
    return groups_len == groups

def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0
    unknow_possibilitys = {}

    for l in lines:
        l = l[:-1]

        springs, groups = l.split(" ")
        springs = list(springs)
        groups = list(map(int, groups.split(",")))

        i = 0
        unknow_range_pos = []
        while i < len(springs):
            unknow_len = get_unknow_len(springs, i)
            if unknow_len > 0:
                if not unknow_len in unknow_possibilitys:
                    unknow_possibilitys[unknow_len] = bruteforce(".#", unknow_len)
                unknow_range_pos.append((i, unknow_len))
                i += unknow_len
            else: i += 1
        
        i = 0
        possibilitys = [[]]
        unknow_range_pos = []
        while i < len(springs):
            unknow_len = get_unknow_len(springs, i)
            if unknow_len > 0:
                tmp = []
                for t in possibilitys:
                    for p in unknow_possibilitys[unknow_len]:
                        tmp.append(t + p)
                possibilitys = tmp
                i += unknow_len
            else:
                for t in possibilitys:
                    t += springs[i]
                i += 1
        
        nb_arrangements = 0
        for p in possibilitys:
            if is_valid(p, groups):
                nb_arrangements += 1
        
        res += nb_arrangements

    return res

def main() -> None:
    # 7204
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    

if __name__  == "__main__":
    main()