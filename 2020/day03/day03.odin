package day03

import "core:fmt"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(grid: []string) -> int {
    res := 0

    col := 0
    row_len := len(grid[0])
    for row in 0 ..< len(grid) {
        if grid[row][col] == '#' {
            res += 1
        }

        col += 3
        col %= row_len
    }

    return res
}

part2 :: proc(grid: []string) -> int {
    Slope :: struct {
        dx: int,
        dy: int,
    }

    res := 0
    slopes := [5]Slope{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}

    row_len := len(grid[0])
    nb_rows := len(grid)
    for i in 0 ..< 5 {
        col := 0
        slope := slopes[i]
        local_res := 0

        for row := 0; row < nb_rows; row += slope.dy {
            if grid[row][col] == '#' {
                local_res += 1
            }

            col += slope.dx
            col %= row_len
        }

        res = local_res if res == 0 else res * local_res
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
