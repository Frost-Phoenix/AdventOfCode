# https://adventofcode.com/2023/day/6


def part_1(file: str):
    
    lines = open(file, 'r').readlines()

    times     = [int(x) for x in lines[0][11:-1].split(" ") if len(x) > 0]
    distances = [int(x) for x in lines[1][11:-1].split(" ") if len(x) > 0]

    res = 1

    for i in range(len(times)):
        t_min, t_max = 0, 0
        time = times[i]
        distance = distances[i]

        for j in range(1, time+1):
            if (time - j) * j > distance:
                t_min = j
                break

        for j in range(time, 0, -1):
            if (time - j) * j > distance:
                t_max = j
                break

        res *= t_max - t_min + 1

    return res


def main():
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")


if __name__ == "__main__":
    main()