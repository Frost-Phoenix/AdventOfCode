package day09

import "core:fmt"
import "core:slice"
import "core:strconv"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

get_invalid_number :: proc(numbers: []int) -> int {
    res := 0
    window := 25

    m := make(map[int]bool)
    loop: for n, i in numbers[window:] {
        idx := i + window

        clear(&m)

        for nb in numbers[idx - window:idx] {
            if m[n - nb] {
                continue loop
            }

            m[nb] = true
        }

        res = n
        break
    }

    return res
}

part1 :: proc(numbers: []int) -> int {
    return get_invalid_number(numbers)
}

part2 :: proc(numbers: []int) -> int {
    invalid_number := get_invalid_number(numbers)

    res := 0

    for n, i in numbers {
        j := i + 1
        sum := n
        for ; sum < invalid_number && j < len(numbers); j += 1 {
            sum += numbers[j]
        }

        if sum == invalid_number {
            res = slice.min(numbers[i:j]) + slice.max(numbers[i:j])
            break
        }
    }

    return res
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    // fmt.println(lines)

    numbers := make([dynamic]int, 0, len(lines))
    for line in lines {
        n, _ := strconv.parse_int(line, 10)
        append(&numbers, n)
    }

    fmt.printfln("Part 1: %v", part1(numbers[:]))
    fmt.printfln("Part 2: %v", part2(numbers[:]))

    free_all(context.temp_allocator)
}
