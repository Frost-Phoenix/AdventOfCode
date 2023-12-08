# https://adventofcode.com/2023/day/4


def get_nb_wining_numbers_per_card(file: str) -> int:
    res = []

    with open(file, "r") as  f:
        for l in f:
            nb_list = l.split(": ")[1][:-1]
            wining_nb, pulled_nb = nb_list.split(" | ")
            wining_nb = wining_nb.split(" ")
            pulled_nb = pulled_nb.split(" ")

            current_score = 0
            for nb in pulled_nb:
                if nb in wining_nb and nb != '':
                    current_score += 1
            res.append(current_score)

    return res

def part_1(file: str) -> int:
    res = 0
    nb_wining_numbers_list = get_nb_wining_numbers_per_card(file)

    for nb in nb_wining_numbers_list:
        res += int(2 ** (nb - 1))

    return res

def part_2(file: str) -> int:
    nb_lines = int(open(file, "r").readlines()[-1].split(':')[0].split("Card ")[1])

    nb_tikets = {}
    for i in range(nb_lines):
        nb_tikets[i] = 1

    nb_wining_numbers_list = get_nb_wining_numbers_per_card(file)
    for i in range(nb_lines):
        for j in range(i + 1, i + nb_wining_numbers_list[i] + 1):
            nb_tikets[j] += nb_tikets[i]

    return sum([val for val in nb_tikets.values()])


def main() -> None:
    # 21568
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")

    # 11827296
    part_2_sol = part_2("input.txt")
    print(f"part 2 sol: {part_2_sol}")


if __name__ == "__main__":
    main()
