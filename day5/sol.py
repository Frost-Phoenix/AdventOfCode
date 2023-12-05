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

def main() -> None:
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")


if __name__ == "__main__":
    main()