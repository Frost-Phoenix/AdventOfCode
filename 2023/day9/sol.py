# https://adventofcode.com/2023/day/ 


def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0

    for l in lines:
        l = l[:-1]

        values = list(map(int, l.split()))
        last_val = values[-1]
        last_changes = [values[-1]]
        
        all_zero = False
        while not all_zero:
            all_zero = True
            new_val = []
            for i in range(1, len(values)):
                step = values[i] - values[i-1]
                new_val.append(step)

                if step != 0: all_zero = False
                
            last_changes.append(values[-1] - values[-2])
            values = new_val

        for i in range(len(last_changes) - 2, -1, -1):
            last_changes[i] += last_changes[i+1]

        res += last_changes[0]

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