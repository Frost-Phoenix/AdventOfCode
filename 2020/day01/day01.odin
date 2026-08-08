package day01

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(values: []int) -> int {
    fmt.println("part1:")

    for v1 in values {
        for v2 in values {
            if v1 + v2 == 2020 {
                fmt.printfln("%v + %v = 2020", v1, v2)
                fmt.printfln("res: %v", v1 * v2)

                return v1 * v2
            }
        }
    }

    return 0
}

part2 :: proc(values: []int) -> int {
    fmt.println("part2:")

    for v1 in values {
        for v2 in values {
            for v3 in values {

                if v1 + v2 + v3 == 2020 {
                    fmt.printfln("%v + %v + %v = 2020", v1, v2, v3)
                    fmt.printfln("res: %v", v1 * v2 * v3)

                    return v1 * v2 * v3
                }
            }
        }
    }

    return 0
}

main :: proc() {
    data, err := os.read_entire_file(INPUT, context.allocator)
    if err != nil {
        fmt.eprintfln("Failed to load the file '%s': %v", INPUT, err)
        os.exit(1)
    }
    defer delete(data)

    file := string(data)
    lines := strings.split_lines(file)
    defer delete(lines)

    values := make([dynamic]int)
    defer delete(values)

    for l in lines {
        val := strconv.parse_int(l) or_continue

        append(&values, val)
    }

    part1(values[:])
    part2(values[:])
}
