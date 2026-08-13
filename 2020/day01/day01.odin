package day01

import "core:fmt"
import "core:strconv"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(values: []int) -> int {
    for v1 in values {
        for v2 in values {
            if v1 + v2 == 2020 {
                return v1 * v2
            }
        }
    }

    return 0
}

part2 :: proc(values: []int) -> int {
    for v1 in values {
        for v2 in values {
            for v3 in values {
                if v1 + v2 + v3 == 2020 {
                    return v1 * v2 * v3
                }
            }
        }
    }

    return 0
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    values := make([dynamic]int)
    defer delete(values)

    for l in lines {
        val := strconv.parse_int(l) or_continue

        append(&values, val)
    }

    fmt.printfln("Part 1: %v", part1(values[:]))
    fmt.printfln("Part 2: %v", part2(values[:]))

    free_all(context.temp_allocator)
}
