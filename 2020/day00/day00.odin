package day00

import "core:fmt"
import "core:strings"

INPUT :: "test.txt"
// INPUT :: "input.txt"

part1 :: proc(lines: []string) -> int {
    return 0
}

part2 :: proc(lines: []string) -> int {
    return 0
}

main :: proc() {
    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file, context.temp_allocator)

    fmt.println(lines)

    fmt.printfln("Part 1: %v", part1(lines))
    fmt.printfln("Part 2: %v", part2(lines))
}
