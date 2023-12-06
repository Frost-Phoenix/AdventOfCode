# https://adventofcode.com/2023/day/6


def solve(times: list[int], distances: list[int]) -> int:
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

def part_1(file: str):
    lines = open(file, 'r').readlines()

    times     = [int(x) for x in lines[0][11:-1].split(" ") if len(x) > 0]
    distances = [int(x) for x in lines[1][11:-1].split(" ") if len(x) > 0]

    return solve(times, distances)

def part_2(file: str):
    lines = open(file, 'r').readlines()

    times     = [x for x in lines[0][11:-1].split(" ") if len(x) > 0]
    distances = [x for x in lines[1][11:-1].split(" ") if len(x) > 0]

    time = int("".join(times))
    distance = int("".join(distances))

    return solve([time], [distance])


def main():
    # 160816
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")

    # 46561107
    part_2_sol = part_2("input.txt")
    print(f"sol part 2: {part_2_sol}")


if __name__ == "__main__":
    main()