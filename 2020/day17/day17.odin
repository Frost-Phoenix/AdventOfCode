package day17

import "core:fmt"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

World :: []Grid
Grid  :: [][]bool

Pos :: struct {
    x, y, z: int,
}

print_grid :: proc(grid: Grid, new_line: bool = true) {
    for row in grid {
        for col in row {
            switch col {
                case true: fmt.print("# ")
                case false: fmt.print(". ")
            }
        }
        fmt.println()
    }

    if new_line {
        fmt.println()
    }
}

print_world :: proc(world: World) {
    for plane, z in world {
        fmt.printfln("Z = %v", z)
        print_grid(plane)
    }
}

create_world :: proc(size: int) -> World {
    world := make(World, size)

    for &plane in world {
        plane = make(Grid, size)
        for &row in plane {
            row = make([]bool, size)
        }
    }

    return world
}

init_world :: proc(world: ^World, initial_plane: [][]byte) {
    z := len(world) / 2
    plane := &world[z]
    offset := (len(plane) - len(initial_plane)) / 2

    for row, r in initial_plane {
        for col, c in row {
            plane[r + offset][c + offset] = true if initial_plane[r][c] == '#' else false
        }
    }
}

get_nb_neighbor :: proc(world: World, pos: Pos) -> int {
    res := 0

    _is_in_bound :: proc(world: World, pos: Pos) -> bool {
        world_size := len(world)

        x_in_bound := 0 <= pos.x && pos.x < world_size
        y_in_bound := 0 <= pos.y && pos.y < world_size
        z_in_bound := 0 <= pos.z && pos.z < world_size

        return x_in_bound && y_in_bound && z_in_bound
    }

    _is_same_pos :: proc(pos1: Pos, pos2: Pos) -> bool {
        return pos1.x == pos2.x && pos1.y == pos2.y && pos1.z == pos2.z
    }

    for z in pos.z - 1 ..= pos.z + 1 {
        for y in pos.y - 1 ..= pos.y + 1 {
            for x in pos.x - 1 ..= pos.x + 1 {
                if !_is_in_bound(world, {x, y, z}) || _is_same_pos(pos, {x, y, z}) {
                    continue
                }

                if world[z][y][x] == true {
                    res += 1
                }
            }
        }
    }

    return res
}

count_active_cells :: proc(world: World) -> int {
    res := 0

    for plane in world {
        for row in plane {
            for cell in row {
                if cell == true {
                    res += 1
                }
            }
        }
    }

    return res
}

simulate :: proc(initial_plane: [][]byte, nb_cycles: int) -> (nb_alive_cells: int) {
    max_world_size := len(initial_plane) + nb_cycles * 2
    world := create_world(max_world_size)
    next_gen := create_world(max_world_size)

    init_world(&world, initial_plane)

    // fmt.printfln("##### Generation %v #####", 0)
    // print_world(world)

    for cycle in 0 ..< nb_cycles {
        for plane, z in world {
            for row, y in plane {
                for cell, x in row {
                    nb_neighbor := get_nb_neighbor(world, {x, y, z})
                    switch cell {
                        case true: next_gen[z][y][x] = nb_neighbor == 2 || nb_neighbor == 3
                        case false: next_gen[z][y][x] = nb_neighbor == 3
                    }
                }
            }
        }

        world, next_gen = next_gen, world

        // fmt.printfln("##### Generation %v #####", cycle + 1)
        // print_world(world)
    }


    return count_active_cells(world)
}

part1 :: proc(grid: [][]byte) -> int {
    return simulate(grid, 6)
}

part2 :: proc(grid: [][]bool) -> int {
    return 0
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    grid := make([][]byte, len(lines))
    for line, i in lines {
        grid[i] = transmute([]byte)line
    }

    fmt.printfln("Part 1: %v", part1(grid))
    // fmt.printfln("Part 2: %v", part2(lines))

    free_all(context.temp_allocator)
}
