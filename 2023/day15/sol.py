# https://adventofcode.com/2023/day/ 


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
    box = {i: [None] * 10 for i in range(256)}

    for l in open(file, 'r').readline().split(','):
        if l[-1] == '-':
            label = l[:-1]
            id = get_hash(label)
            if any(filter(lambda x: False if x == None else label in x, box[id])):
                tmp = []
                for lens in box[id]:
                    if lens != None and label not in lens:
                        tmp.append(lens)
                box[id] = tmp + [None] * (10 - len(tmp))
        else: 
            label = l[:-2]
            id = get_hash(label)
            if any(filter(lambda x: False if x == None else label in x, box[id])):
                for i in range(len(box[id])):
                    if label in box[id][i]:
                        box[id][i] = l.replace("=", " ")
                        break
            else:
                for i in range(len(box[id])):
                    if box[id][i] == None:
                        box[id][i] = l.replace("=", " ")
                        break

    res = 0
    for i,b in box.items():
        for j,item in enumerate(b):
            if item != None:
                res += (i+1) * (j+1) * int(item[-1])

    return res

def main() -> None:
    # 521341
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    
    # 
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()