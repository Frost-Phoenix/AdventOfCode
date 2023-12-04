# https://adventofcode.com/2023/day/4


def part_1(file: str) -> int:
    sum = 0
    
    with open(file, "r") as  f:
        for l in f:
            nb_list = l.split(": ")[1][:-1]
            wining_nb, pulled_nb = nb_list.split(" | ")
            wining_nb = wining_nb.split(" ")
            pulled_nb = pulled_nb.split(" ")
            
            current_score = 0
            for nb in pulled_nb:
                if nb in wining_nb and nb != '':
                    if current_score == 0:
                        current_score = 1
                    else: current_score *= 2

            sum += current_score
                    
    return sum


def main():
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")


if __name__ == "__main__":
    main()
