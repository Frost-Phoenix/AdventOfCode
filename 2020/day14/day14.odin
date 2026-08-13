package day14

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strings"

// INPUT :: "test1.txt"
// INPUT :: "test2.txt"
INPUT :: "input.txt"

part1 :: proc(lines: []string) -> u64 {
    memory := make(map[int]u64)
    mask_or: u64 = 0 // keep the 1 from mask
    mask_and: u64 = 0 // keep the 0 from mask

    for line in lines {
        split := strings.split(line, " = ")
        operator := split[0]
        value := split[1]

        if operator == "mask" {
            mask_or = 0
            mask_and = (1 << 36) - 1

            for i := 0; i < len(value); i += 1 {
                switch value[len(value) - 1 - i] {
                    case '0': mask_and &= ~(1 << uint(i))
                    case '1': mask_or |= 1 << uint(i)
                }
            }
        } else if operator[:3] == "mem" {
            ok: bool
            addr: int
            value_int: u64

            value_int, ok = strconv.parse_u64(value)
            assert(ok, "failed to parse memory value")

            addr, ok = strconv.parse_int(operator[4:len(operator) - 1], 10)
            assert(ok, "failed to parse memory address")

            memory[addr] = (value_int | mask_or) & mask_and
        } else {
            panic("unknown operator")
        }
    }

    res: u64
    for _, v in memory {
        res += v
    }

    return res
}

part2 :: proc(lines: []string) -> u64 {
    memory := make(map[u64]u64)
    mask: string

    update_mem :: proc(memory: ^map[u64]u64, mask: string, addr: u64, val: u64) {
        if len(mask) == 0 {
            memory[addr] = val
            return
        }

        i := len(mask) - 1
        switch mask[0] {
            case '0': update_mem(memory, mask[1:], addr, val)
            case '1': update_mem(memory, mask[1:], addr | (1 << u64(i)), val)
            case 'X':
                update_mem(memory, mask[1:], addr | (1 << u64(i)), val)
                update_mem(memory, mask[1:], addr & ~(1 << u64(i)), val)
            case: panic("unknown mask character")
        }
    }

    for line in lines {
        split := strings.split(line, " = ")
        operator := split[0]
        value := split[1]

        if operator == "mask" {
            mask = value
        } else if operator[:3] == "mem" {
            ok: bool
            addr, value_int: u64

            value_int, ok = strconv.parse_u64(value)
            assert(ok, "failed to parse memory value")

            addr, ok = strconv.parse_u64(operator[4:len(operator) - 1], 10)
            assert(ok, "failed to parse memory address")

            update_mem(&memory, mask, addr, value_int)
        } else {
            panic("unknown operator")
        }
    }

    res: u64
    for _, v in memory {
        res += v
    }

    return res
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    // fmt.println(lines)

    fmt.printfln("Part 1: %v", part1(lines))
    fmt.printfln("Part 2: %v", part2(lines))

    free_all(context.temp_allocator)
}
