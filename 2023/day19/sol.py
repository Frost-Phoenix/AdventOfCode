# https://adventofcode.com/2023/day/19


def parse_input(file: str) -> (dict[str: list[str]], list[list[int]]):
    workflows, parts = open(file, 'r').read().split('\n\n')

    workflows = {w.split('{')[0]: w.replace('}', '').split('{')[1].split(',') for w in workflows.split()}

    parts = [list(map(int,
        p[1:-1].replace('x=', '')
               .replace('m=', '')
               .replace('a=', '')
               .replace('s=', '')
               .split(',')))
        for p in parts.split('\n')
    ]

    return (workflows, parts)

def process_rules(rules: list[str], part: list[int]) -> str:
    var = {'x': 0, 'm': 1, 'a': 2, 's': 3}
    
    for r in rules:
        if r == rules[-1]: return r

        nb = part[var[r[0]]]
        value = int(r.split(':')[0][2:])

        if (r[1] == '>' and nb > value or
            r[1] == '<' and nb < value):
            return r.split(':')[1]

def process_part(workflows: dict[str: list[str]], part: list[int]) -> bool:
    current_w = "in"

    done = False
    while not done:
        rules = workflows[current_w]
        next_w = process_rules(rules, part)

        if (next_w == 'A'): return True
        if (next_w == 'R'): return False

        current_w = next_w

    return False

def part_1(file: str) -> int:
    res = 0
    
    workflows, parts = parse_input(file)
    
    return sum([sum(p) for p in parts if (process_part(workflows, p))])

def main() -> None:
    # 487623
    part_1_sol = part_1("input.txt")
    print(f"sol part 1: {part_1_sol}")
    

if __name__  == "__main__":
    main()