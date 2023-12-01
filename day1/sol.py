# https://adventofcode.com/2023/day/1


def part_1(file: str) -> int:
    """Compute the sum of all first and second digit of each line in the file
    
    Args:
        :file (str): input file
    
    Returns:
        int: sum 
    """

    sum = 0
    line_nb = 0

    with open(file, "r") as f:
        for l in f:
            for c in l:
                if c.isdigit():
                    line_nb += int(c) * 10
                    break
            for c in reversed(l):
                if c.isdigit():
                    line_nb += int(c)
                    break
            sum += line_nb
            line_nb = 0

    return sum

def part_2(file: str) -> int:
    valide_words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    sum = 0
    line_nb = 0

    with open(file, "r") as f:
        for l in f:
            for c in l:
                if c.isdigit():
                    line_nb += int(c) * 10
                    break
            for c in reversed(l):
                if c.isdigit():
                    line_nb += int(c)
                    break
            sum += line_nb
            line_nb = 0

    return sum


def main() -> None:
    sum_part_1 = part_1("input.txt")
    print(f"part 1 sol : {sum_part_1}")

    sum_part_2 = part_2("input.txt")
    print(f"part 2 sol : {sum_part_2}")


if __name__ == "__main__":
    main()