# https://adventofcode.com/2023/day/7

from collections import Counter


def get_sum(hands: list[(str,int)], nb_hands: int, power) -> int:
    sum = 0

    for l in hands:
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

def part_1(file: str) -> int:
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

    return get_sum(hands.values(), nb_hands, power)

def part_2(file: str):
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
            val = Counter(hand)

            j_val = val['J']
            max_score = j_val
            max_score_c = "J"
            for k,v in val.items():
                if k != "J" and v + j_val > max_score:
                    max_score = v + j_val
                    max_score_c = k

            done = False
            if max_score == 2:
                seen = False
                for v in val.values():
                    if v == 2 and val['J'] != 2:
                        if not seen: seen = True
                        else: 
                            hands["two_pair"].append((hand,bid))
                            done = True
                            break
            if not done:
                if   5 == max_score: hands["five_of_a_kind"].append((hand,bid))
                elif 4 == max_score: hands["four_of_a_kind"].append((hand,bid))
                elif 3 == max_score:
                    ok = False
                    if 2 in val.values() and j_val != 2: 
                        for k,v in val.items():
                            if v == 2 and k != max_score_c:
                                hands["full_house"].append((hand,bid))
                                ok = True
                                break
                    if not ok: hands["three_of_a_kind"].append((hand,bid))
                elif 2 == max_score: hands["one_pair"].append((hand,bid))
                else: hands["high_card"].append((hand,bid))

    def power(c: str) -> int:
        if c.isdigit(): return int(c)
        else: return {"A": 14, "K": 13, "Q": 12, "T": 10, "J": 0}[c]

    return get_sum(hands.values(), nb_hands, power)

def main():
    # 249483956
    part_1_sol = part_1("input.txt")
    print(f"part 1 sol: {part_1_sol}")

    # 252137472
    part_2_sol = part_2("input.txt")
    print(f"part 2 sol: {part_2_sol}")


if __name__ == "__main__":
    main()