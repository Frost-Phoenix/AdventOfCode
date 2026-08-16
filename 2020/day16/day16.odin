package day16

import "core:fmt"
import "core:strconv"
import "core:strings"

// INPUT :: "test1.txt"
// INPUT :: "test2.txt"
INPUT :: "input.txt"

Range :: struct {
    start: int,
    end:   int,
}

Field :: struct {
    name:   string,
    ranges: [2]Range,
}

fields: []Field

parse_ticket :: proc(ticket_string: string) -> []int {
    ticket_split := strings.split(ticket_string, ",")
    ticket := make([]int, len(ticket_split))

    for nb, i in ticket_split {
        nb_int, ok := strconv.parse_int(nb, 10)
        assert(ok, "failed to parse ticket")

        ticket[i] = nb_int
    }

    return ticket
}

get_valid_tickets :: proc(
    fields_list: []string,
    other_tickets: []string,
) -> (
    valid_tickets: [dynamic][]int,
    error_rate: int,
) {
    valid: [1000]bool
    fields = make([]Field, len(fields_list))

    for field, i in fields_list {
        field_split := strings.split(field, ": ")
        field_name := field_split[0]
        ranges := strings.split(field_split[1], " or ")

        fields[i].name = field_name

        for range, j in ranges {
            range_split := strings.split(range, "-")
            start := strconv.parse_int(range_split[0], 10) or_else panic("failed to parse range")
            end := strconv.parse_int(range_split[1], 10) or_else panic("failed to parse range")

            fields[i].ranges[j] = {start, end}

            for i := start; i <= end; i += 1 {
                valid[i] = true
            }
        }
    }

    error_rate = 0
    valid_tickets = make([dynamic][]int, 0, len(other_tickets))
    loop: for t in other_tickets {
        values := parse_ticket(t)
        for v in values {
            if !valid[v] {
                error_rate += v
                continue loop
            }
        }

        append(&valid_tickets, values)
    }

    return
}

part1 :: proc(fields_list: []string, other_tickets: []string) -> int {
    _, error_rate := get_valid_tickets(fields_list, other_tickets)
    return error_rate
}

is_in_range :: proc(n: int, ranges: []Range) -> bool {
    range1 := ranges[0]
    range2 := ranges[1]
    return (range1.start <= n && n <= range1.end) || (range2.start <= n && n <= range2.end)
}

remove_value :: proc(list: ^[dynamic]int, val: int) {
    for v, i in list {
        if v == val {
            unordered_remove(list, i)
            break
        }
    }
}

part2 :: proc(fields_list: []string, ticket_str: string, other_tickets: []string) -> int {
    valid_tickets, _ := get_valid_tickets(fields_list, other_tickets)

    possible_idx := make([][dynamic]int, len(fields))

    ticket := parse_ticket(ticket_str)
    ticket_len := len(ticket)

    for &field, i in fields {
        search_col: for col in 0 ..< ticket_len {
            for t in valid_tickets {
                if !is_in_range(t[col], field.ranges[:]) {
                    continue search_col
                }
            }

            append(&possible_idx[i], col)
        }
    }

    found_cols := make([]bool, len(fields))

    for {
        found_duplicates := false

        for p, i in possible_idx {
            if len(p) == 1 && !found_cols[p[0]] {
                for &index_list, j in possible_idx {
                    if i == j {
                        continue
                    }

                    remove_value(&index_list, p[0])
                }

                found_duplicates = true
                found_cols[p[0]] = true
            }
        }

        if !found_duplicates {
            break
        }
    }

    res := 1
    for field, i in fields {
        if !strings.starts_with(field.name, "departure") {
            continue
        }

        res *= ticket[possible_idx[i][0]]
    }

    return res
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    parts := strings.split(file, "\n\n")

    fields_list := strings.split_lines(parts[0])
    ticket := strings.split_lines(parts[1])[1]
    other_tickets := strings.split_lines(parts[2])[1:]

    fmt.printfln("Part 1: %v", part1(fields_list, other_tickets))
    fmt.printfln("Part 2: %v", part2(fields_list, ticket, other_tickets))

    free_all(context.temp_allocator)
}
