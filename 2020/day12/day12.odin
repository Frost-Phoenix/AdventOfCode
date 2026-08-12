package day12

import "core:fmt"
import "core:strconv"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

Position :: struct {
    x: int,
    y: int,
}

Direction :: enum {
    North,
    East,
    West,
    South,
}

Instruction_Type :: enum {
    Move_Forward,
    Move_North,
    Move_South,
    Move_East,
    Move_West,
    Turn_Left,
    Turn_Right,
}

Instruction :: struct {
    type:  Instruction_Type,
    value: int,
}

parse_instructions :: proc(lines: []string) -> []Instruction {
    instructions := make([]Instruction, len(lines))

    for line, i in lines {
        instruction := &instructions[i]
        switch line[0] {
            case 'F': instruction.type = .Move_Forward
            case 'N': instruction.type = .Move_North
            case 'S': instruction.type = .Move_South
            case 'E': instruction.type = .Move_East
            case 'W': instruction.type = .Move_West
            case 'L': instruction.type = .Turn_Left
            case 'R': instruction.type = .Turn_Right
            case: panic("Unknown instruction")
        }

        value, ok := strconv.parse_int(line[1:], 10)
        assert(ok, "failed to parse instruction value")

        instruction.value = value
    }

    return instructions
}

part1 :: proc(lines: []string) -> int {
    instructions := parse_instructions(lines)

    turn :: proc(type: Instruction_Type, value: int, dir: ^Direction) {
        assert(type == .Turn_Right || type == .Turn_Left)

        multiplier := 1 if type == .Turn_Right else 3
        for _ in 0 ..< value / 90 * multiplier {
            switch dir^ {
                case .North: dir^ = .East
                case .South: dir^ = .West
                case .East: dir^ = .South
                case .West: dir^ = .North
            }
        }
    }

    move_forward :: proc(dir: Direction, value: int, pos: ^Position) {
        switch dir {
            case .North: pos.y += value
            case .South: pos.y -= value
            case .East: pos.x += value
            case .West: pos.x -= value
        }
    }

    current_dir := Direction.East
    current_pos := Position{0, 0}
    for instruction in instructions {
        switch instruction.type {
            case .Move_Forward: move_forward(current_dir, instruction.value, &current_pos)
            case .Move_North: current_pos.y += instruction.value
            case .Move_South: current_pos.y -= instruction.value
            case .Move_East: current_pos.x += instruction.value
            case .Move_West: current_pos.x -= instruction.value
            case .Turn_Left, .Turn_Right: turn(instruction.type, instruction.value, &current_dir)
        }
    }

    distance := abs(current_pos.x) + abs(current_pos.y)

    return distance
}

part2 :: proc(lines: []string) -> int {
    instructions := parse_instructions(lines)

    turn :: proc(type: Instruction_Type, value: int, waypoint: ^Position) {
        assert(type == .Turn_Right || type == .Turn_Left)

        multiplier := 1 if type == .Turn_Right else 3
        for _ in 0 ..< value / 90 * multiplier {
            waypoint.x, waypoint.y = waypoint.y, waypoint.x * -1
        }
    }

    waypoint := Position{10, 1}
    current_pos := Position{0, 0}
    for instruction in instructions {
        switch instruction.type {
            case .Move_Forward:
                current_pos.x += instruction.value * waypoint.x
                current_pos.y += instruction.value * waypoint.y
            case .Move_North: waypoint.y += instruction.value
            case .Move_South: waypoint.y -= instruction.value
            case .Move_East: waypoint.x += instruction.value
            case .Move_West: waypoint.x -= instruction.value
            case .Turn_Left, .Turn_Right: turn(instruction.type, instruction.value, &waypoint)
        }
    }

    distance := abs(current_pos.x) + abs(current_pos.y)


    return distance
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
