# https://adventofcode.com/2023/day/7

from collections import Counter


def part_1(file: str) -> int:
    sum = 0
    
    nb_hands = 0
    hands = {
        "five_of_a_kind": [], 
        "four_of_a_kind": [], 
        "full_house": [], 
        "three_of_a_kind": [], 
        "two_pair": [],
        "one_pair": [],
        "high_card": []
    }

    with open(file, 'r') as f:
        for l in f:
            nb_hands += 1
            hand, bid = l[:-1].split()
            bid = int(bid)
            val = Counter(hand).values()

            seen = False
            for v in val:
                if v == 2:
                    if not seen: seen = True
                    else: 
                        hands["two_pair"].append((hand,bid))
                        break
            else:
                if 5 in val: hands["five_of_a_kind"].append((hand,bid))
                elif 4 in val: hands["four_of_a_kind"].append((hand,bid))
                elif 3 in val and 2 in val: hands["full_house"].append((hand,bid))
                elif 3 in val: hands["three_of_a_kind"].append((hand,bid))
                elif 2 in val: hands["one_pair"].append((hand,bid))
                else: hands["high_card"].append((hand,bid))

    def power(c: str) -> int:
        if c.isdigit(): return int(c)
        else: return {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}[c]

    for l in hands.values():
        used = []
        for i in range(len(l)):
            current_max = None
            for e in l:
                if e not in used:
                    current_max = e
                    break
            for hand, bid in l:
                if (hand, bid) not in used and current_max != (hand, bid):
                    for i in range(len(hand)):
                        power_dif = power(hand[i]) - power(current_max[0][i])
                        if power_dif > 0: current_max = (hand, bid)
                        elif power_dif < 0: break
            used.append(current_max)
            sum += current_max[1] * nb_hands
            nb_hands -= 1

    return sum


def main():
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")


if __name__ == "__main__":
    main()