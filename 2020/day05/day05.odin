package day05

import "core:fmt"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

get_seat :: proc(ticket: string) -> (row: int, col: int) {
    start := 0
    end := 127
    remaining := 128

    for c in ticket[:7] {
        remaining /= 2
        switch c {
            case 'F': end -= remaining
            case 'B': start += remaining
        }
    }
    row = start

    start = 0
    end = 7
    remaining = 8

    for c in ticket[7:] {
        remaining /= 2
        switch c {
            case 'L': end -= remaining
            case 'R': start += remaining
        }
    }
    col = start

    return
}

get_seat_id_from_seat :: proc(row: int, col: int) -> int {
    return row * 8 + col
}

get_seat_id_from_ticket :: proc(ticket: string) -> int {
    row, col := get_seat(ticket)
    return get_seat_id_from_seat(row, col)
}

get_seat_id :: proc {
    get_seat_id_from_seat,
    get_seat_id_from_ticket,
}

part1 :: proc(lines: []string) -> int {
    res := 0

    for line in lines {
        row, col := get_seat(line)
        seat_id := get_seat_id(row, col)

        // fmt.printfln("%v: row=%v, col=%v, seat_id=%v", line, row, col, seat_id)

        if seat_id > res {
            res = seat_id
        }
    }

    return res
}

part2 :: proc(lines: []string) -> int {
    res := 0

    ids := make(map[int]bool, context.temp_allocator)

    for line in lines {
        seat_id := get_seat_id(line)
        ids[seat_id] = true
    }

    for key in ids {
        if ids[key - 2] && !(key - 1 in ids) {
            res = key - 1
            break
        }
        if ids[key + 2] && !(key + 1 in ids) {
            res = key + 1
            break
        }
    }

    return res
}

main :: proc() {
    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file, context.temp_allocator)

    // fmt.printfln("%#v", lines)

    fmt.print("Part 1: ")
    sol1 := part1(lines)
    fmt.println(sol1)

    fmt.print("Part 2: ")
    sol2 := part2(lines)
    fmt.println(sol2)
}
