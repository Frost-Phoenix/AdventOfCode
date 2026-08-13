package day02

import "core:fmt"
import "core:strconv"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(lines: []string) -> int {
    res := 0
    for l in lines {
        split := strings.split_multi(l, {"-", " ", ": "}) or_continue

        min := strconv.parse_int(split[0], 10) or_continue
        max := strconv.parse_int(split[1], 10) or_continue
        letter := split[2]
        password := split[3]

        count := strings.count(password, letter)

        if min <= count && count <= max {
            res += 1
        }
    }

    return res
}

part2 :: proc(lines: []string) -> int {
    res := 0
    for l in lines {
        split := strings.split_multi(l, {"-", " ", ": "}) or_continue

        p1 := (strconv.parse_int(split[0], 10) or_continue) - 1
        p2 := (strconv.parse_int(split[1], 10) or_continue) - 1
        letter := split[2][0]
        password := split[3]

        if (password[p1] == letter || password[p2] == letter) && password[p1] != password[p2] {
            res += 1
        }
    }

    return res
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    fmt.printfln("Part 1: %v", part1(lines))
    fmt.printfln("Part 2: %v", part2(lines))

    free_all(context.temp_allocator)
}
