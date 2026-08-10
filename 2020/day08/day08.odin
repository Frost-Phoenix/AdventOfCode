package day08

import "core:fmt"
import "core:strconv"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(lines: []string) -> int {
    pc := 0
    acc := 0

    instruction_ran := make(map[int]bool)

    for {
        if instruction_ran[pc] || pc == len(lines) {
            break
        }

        instruction := lines[pc]
        opcode := instruction[:3]
        opperand := strconv.parse_int(instruction[4:], 10) or_continue

        instruction_ran[pc] = true

        switch opcode {
            case "acc": acc += opperand
            case "jmp": pc += opperand - 1
            case "nop":
        }

        pc += 1
    }

    return acc
}

part2 :: proc(lines: []string) -> int {
    instruction_ran := make(map[int]bool)

    solve :: proc(
        pc: int,
        acc: int,
        lines: []string,
        instruction_ran: ^map[int]bool,
        changed: bool,
    ) -> (
        res: int,
        ok: bool,
    ) {
        if pc == len(lines) {
            return acc, true
        } else if instruction_ran[pc] {
            return 0, false
        }

        pc := pc
        acc := acc

        instruction := lines[pc]
        opcode := instruction[:3]
        opperand, _ := strconv.parse_int(instruction[4:], 10)

        instruction_ran[pc] = true
        defer delete_key(instruction_ran, pc)

        switch opcode {
            case "acc": acc += opperand
            case "jmp": pc += opperand - 1
            case "nop":
        }

        res, ok = solve(pc + 1, acc, lines, instruction_ran, changed)
        if !ok && !changed {
            switch opcode {
                case "nop": pc += opperand - 1 // transform to jmp
                case "jmp": pc -= opperand - 1 // transform to nop, undo jump
            }

            return solve(pc + 1, acc, lines, instruction_ran, true)
        }

        return
    }

    res, ok := solve(0, 0, lines, &instruction_ran, false)
    if !ok {
        fmt.eprintln("No solution found")
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
