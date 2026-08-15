package day15

import "core:fmt"
import "core:strconv"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

get_nth_spoken_number :: proc(numbers: []int, n: int) -> int {
    turn := 1
    last: int
    seen := make(map[int][2]int) // map number to the turns where it was spoken

    for nb in numbers {
        seen[nb] = {turn, 0}
        last = nb
        turn += 1
    }

    add_seen :: proc(seen: ^map[int][2]int, last: int, turn: int) {
        new_entry, present := seen[last]
        if !present {
            seen[last] = {turn, 0}
        } else {
            seen[last] = {turn, new_entry[0]}
        }
    }

    for ; turn <= n; turn += 1 {
        last_entry := seen[last]

        if last_entry[1] == 0 {
            last = 0
        } else {
            last = last_entry[0] - last_entry[1]
        }

        add_seen(&seen, last, turn)
    }

    return last
}

part1 :: proc(numbers: []int) -> int {
    return get_nth_spoken_number(numbers, 2020)
}

part2 :: proc(numbers: []int) -> int {
    return get_nth_spoken_number(numbers, 30000000)
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    // fmt.println(lines)

    numbers_string := strings.split(lines[0], ",")
    numbers := make([]int, len(numbers_string))

    for nb_str, i in numbers_string {
        nb, ok := strconv.parse_int(nb_str, 10)
        assert(ok, "failed to parse number")

        numbers[i] = nb
    }

    fmt.printfln("Part 1: %v", part1(numbers))
    fmt.printfln("Part 2: %v", part2(numbers))

    free_all(context.temp_allocator)
}
