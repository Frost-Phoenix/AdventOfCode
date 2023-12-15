# https://adventofcode.com/2022/day/2


def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0
    val = ord('X') - 1
    move = {'A': 'Z', 'B': 'X', 'C': 'Y', 'X': 'C', 'Y': 'A', 'Z': 'B'}

    for l in lines:
        opponent, you = l[:-1].split(' ')
        res += ord(you) - val

        if move[you] == opponent: res += 6
        elif move[opponent] != you: res += 3

    return res

def part_2(file: str) -> int:
    lines = open(file, 'r').readlines()

    res = 0
    points = {'X': 0, 'Y': 3, 'Z': 6}
    move = {
        'A': {'X': 3, 'Y': 1, 'Z': 2}, 
        'B': {'X': 1, 'Y': 2, 'Z': 3}, 
        'C': {'X': 2, 'Y': 3, 'Z': 1}
    }

    for l in lines:
        opponent, goal = l[:-1].split(' ')
        res += move[opponent][goal] + points[goal]

    return res

def main() -> None:
    # 11449
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")

    # 13187
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__  == "__main__":
    main()