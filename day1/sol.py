# https://adventofcode.com/2023/day/1


def part_1(file: str) -> int:
    """Compute the sum of all first and last digit of each line in the file
    
    Args:
        :file (str): input file
    
    Returns:
        int: sum 
    """

    def solve_line(line: str) -> int:
        for c in line:
            if c.isdigit():
                return int(c)

    sum = 0

    with open(file, "r") as f:
        for l in f:
            sum += solve_line(l) * 10 + solve_line(reversed(l))            

    return sum

def part_2(file: str) -> int:
    """Same as part one but account for digit spells with letters
    
    Args:
        :file (str): input file
    
    Returns:
        int: sum 
    """

    valide_words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    sum = 0

    def solve_line(line: str, backwards: int = False) -> int:
        buffer = ""
        for c in line:
            if c.isdigit():
                return int(c)
            else:
                if len(buffer) < 5: buffer += c
                else: buffer = buffer[1:] + c

                tmp_buffer = buffer if not backwards else buffer[::-1]

                for k in valide_words.keys():
                    if k in tmp_buffer:
                        return valide_words[k]
                    
    with open(file, "r") as f:
        for l in f:
            sum += solve_line(l) * 10 + solve_line(reversed(l), backwards=True)
            line_nb = 0

    return sum


def main() -> None:
    sum_part_1 = part_1("input.txt")
    print(f"part 1 sol : {sum_part_1}")

    sum_part_2 = part_2("input.txt")
    print(f"part 2 sol : {sum_part_2}")


if __name__ == "__main__":
    main()