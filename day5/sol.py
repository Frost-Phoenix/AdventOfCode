# https://adventofcode.com/2023/day/5


def part_1(file: str) -> int:
    file_lines = open(file).read()
    source = [int(nb) for nb in file_lines.split("\n")[0].split("seeds: ")[1].split(" ")]

    file_lines = file_lines.split("\n\n")[1:]

    for l in file_lines:
        res = [None] * len(source)
        for dest in l.split("\n")[1:]:
            dest = dest.split(" ")
            range_len = int(dest[2])
            source_range = range(int(dest[1]), int(dest[1]) + range_len)
            dest_range = range(int(dest[0]), int(dest[0]) + range_len)

            for i,nb in enumerate(source):
                if nb in source_range:
                    if res[i] == None:
                        res[i] = dest_range[source_range.index(nb)]

        for i in range(len(res)):
            if res[i] == None:
                res[i] = source[i]

        source = res

    return min(source)


def part_2(file: str) -> int:
    # Thank's to https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py
    
    file_lines = open(file).read()
    seeds = [int(nb) for nb in file_lines.split("\n")[0].split("seeds: ")[1].split(" ")]
    file_lines = file_lines.split("\n\n")[1:]

    source_ranges = []
    i , n = 0, len(seeds)
    while i < n:
        source_ranges.append((seeds[i], seeds[i] + seeds[i+1]))
        i += 2
        
    for l in file_lines:
        res = [] 
        dest_list = l.split("\n")[1:]
        for s, e in source_ranges:
            for dest in dest_list:
                dest_s, source_s, l = [int(e) for e in dest.split(" ")]
                inter_s = max(s, source_s)
                inter_e = min(e, source_s + l)
                # Got an intersection
                if inter_s < inter_e:
                    res.append((inter_s - source_s + dest_s, inter_e - source_s + dest_s))
                    if inter_s > s: source_ranges.append((s, inter_s))
                    if inter_e < e: source_ranges.append((inter_e, e))
                    break
            else:
                res.append((s, e))
        
        source_ranges = res
        
    return(min(res)[0])

def main() -> None:
    # 486613012
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")

    # 56931769
    part_2_sol = part_2("input.txt")
    print(f"part 2 sol: {part_2_sol}")


if __name__ == "__main__":
    main()