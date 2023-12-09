# https://adventofcode.com/2023/day/ 


def solve(file: str, part: int) -> int:
    lines = open(file, 'r').readlines()

    res = 0

    for l in lines:
        l = l[:-1]

        values = list(map(int, l.split()))
        last_val = values[-1]
        changes = [values[-1 if part == 1 else 0]] 
        
        all_zero = False
        while not all_zero:
            all_zero = True
            new_val = []
            for i in range(1, len(values)):
                step = values[i] - values[i-1]
                new_val.append(step)

                if step != 0: all_zero = False

            if part == 1: changes.append(values[-1] - values[-2])
            else: changes.append(values[1] - values[0])
            values = new_val

        for i in range(len(changes) - 2, -1, -1):
            if part == 1: changes[i] += changes[i+1]
            else: changes[i] -= changes[i+1]

        res += changes[0]

    return res

def main() -> None:
    # 1898776583
    part_1_sol = solve("input.txt", 1)
    print(f"sol part 1: {part_1_sol}")
    
    # 1100
    part_2_sol = solve("input.txt", 2)
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()