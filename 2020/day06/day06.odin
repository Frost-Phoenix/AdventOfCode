package day06

import "core:fmt"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(groups: []string) -> int {
    res := 0

    for group in groups {
        yes: bit_set['a' ..= 'z'] = {}

        for person in strings.split_lines(group, context.temp_allocator) {
            for answer in person {
                yes += {answer}
            }
        }

        res += card(yes)
    }

    return res
}

part2 :: proc(groups: []string) -> int {
    res := 0

    for group in groups {
        yes := make(map[rune]int, context.temp_allocator)

        persons := strings.split_lines(group, context.temp_allocator)
        for person in persons {
            for answer in person {
                yes[answer] += 1
            }
        }

        nb_persons := len(persons)
        for _, val in yes {
            if val == nb_persons {
                res += 1
            }
        }
    }

    return res
}

main :: proc() {
    data := #load(INPUT)
    file := string(data)
    groups := strings.split(file, "\n\n", context.temp_allocator)

    // fmt.println(groups)

    fmt.printfln("Part 1: %v", part1(groups))
    fmt.printfln("Part 2: %v", part2(groups))
}
