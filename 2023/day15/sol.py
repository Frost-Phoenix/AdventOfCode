# https://adventofcode.com/2023/day/15


def get_hash(seq: str) -> int:
    res = 0
    for c in seq:
        res += ord(c)
        res *= 17
        res %= 256

    return res

def part_1(file: str) -> int:
    return sum([get_hash(l) for l in open(file, 'r').readline().split(",")])

def part_2(file: str) -> int:
    box = [[] for i in range(256)]

    for l in open(file, 'r').readline().split(','):
        label = l[:-1] if "-" in l else l[:-2]
        id = get_hash(label)
        is_in = any(filter(lambda x: False if x == None else label in x, box[id]))

        if l[-1] == '-': 
            if is_in: box[id] = list(filter(lambda x: label not in x, box[id]))
        elif not is_in: 
            box[id].append(l.replace("=", " "))
        else:
            for i in range(len(box[id])):
                if label in box[id][i]:
                    box[id][i] = l.replace("=", " ")
                    break

    return sum([sum([(i+1) * (j+1) * int(item[-1]) for j,item in enumerate(b)]) for i,b in enumerate(box)])

def main() -> None:
    # 521341
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 252782
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()