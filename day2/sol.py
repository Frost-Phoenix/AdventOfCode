import re

# https://adventofcode.com/2023/day/2


def part_1(file: str) -> int:
    sum = 0
    max_nb_cubes = {"red": 12, "green": 13, "blue": 14}

    with open(file, "r") as f:
        for l in f:
            game_possible = True

            game_id, game_info = l.split(":")
            game_id = int(game_id[5:])
            game_info = game_info.rstrip()

            for cubes in re.split("[;|,]", game_info):
                nb_cubes, cube_color = cubes[1:].split(" ")
                if int(nb_cubes) > max_nb_cubes[cube_color]: game_possible = False
    
            if game_possible: sum += game_id

    return sum


def main():
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")


if __name__ == "__main__":
    main()
