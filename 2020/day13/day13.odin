package day13

import "core:fmt"
import "core:strconv"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(start_timestamp: int, IDs: []string) -> int {
    ids_int := make([]int, len(IDs))
    current_bus_time := make([]int, len(IDs))
    for id, i in IDs {
        id_int := strconv.parse_int(id, 10) or_else -1
        ids_int[i] = id_int

        if id_int == -1 {
            current_bus_time[i] = -1
        } else {
            current_bus_time[i] = start_timestamp % id_int
        }
    }

    res := 0
    timestamp := start_timestamp

    found := false
    for !found {
        for id, i in ids_int {
            if current_bus_time[i] == -1 {
                continue
            } else if current_bus_time[i] % id == 0 {
                wait := timestamp - start_timestamp
                res = wait * id

                found = true
                break
            }

            current_bus_time[i] += 1
        }

        timestamp += 1
    }

    return res
}

part2 :: proc(IDs: []string) -> int {
    offset := 0
    offsets := make([]int, len(IDs))
    ids_int := make([]int, len(IDs))
    for id, i in IDs {
        id_int, ok := strconv.parse_int(id, 10)
        if ok {
            ids_int[i] = id_int
            offsets[i] = (id_int - (offset % id_int)) % id_int
        }

        offset += 1
    }

    M := 1
    for id in ids_int {
        M *= id if id != 0 else 1
    }

    Ms := make([]int, len(IDs))
    for id, i in ids_int {
        if id == 0 {
            continue
        }

        Ms[i] = M / id
    }

    Ms_ineverse := make([]int, len(ids_int))
    for Mi, i in Ms {
        if ids_int[i] == 0 {
            continue
        }

        for j in 1 ..< ids_int[i] {
            if Mi * j % ids_int[i] == 1 {
                Ms_ineverse[i] = j
                break
            }
        }
    }

    t := 0
    for i in 0 ..< len(ids_int) {
        t += offsets[i] * Ms[i] * Ms_ineverse[i]
    }

    return t % M
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    // fmt.println(lines)

    start_timestamp, ok := strconv.parse_int(lines[0], 10)
    assert(ok, "fialed to parse start timestamp")

    IDs := strings.split(lines[1], ",")

    fmt.printfln("Part 1: %v", part1(start_timestamp, IDs))
    fmt.printfln("Part 2: %v", part2(IDs))

    free_all(context.temp_allocator)
}
