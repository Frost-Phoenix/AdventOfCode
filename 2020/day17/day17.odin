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

World4D :: []World

Pos4D :: struct {
    x, y, z, w: int,
}

create_world_4d :: proc(size: int) -> World4D {
    world := make(World4D, size)

    for &world3d in world {
        world3d = make(World, size)
        for &plane in world3d {
            plane = make(Grid, size)
            for &row in plane {
                row = make([]bool, size)
            }
        }
    }

    return world
}

init_world_4d :: proc(world: ^World4D, initial_plane: [][]byte) {
    w := len(world) / 2
    z := len(world) / 2
    world3d := world[w]
    plane := world3d[z]
    offset := (len(plane) - len(initial_plane)) / 2

    for row, r in initial_plane {
        for col, c in row {
            plane[r + offset][c + offset] = true if initial_plane[r][c] == '#' else false
        }
    }
}

get_nb_neighbor_4d :: proc(world: World4D, pos: Pos4D) -> int {
    res := 0

    _is_in_bound :: proc(world: World4D, pos: Pos4D) -> bool {
        world_size := len(world)

        x_in_bound := 0 <= pos.x && pos.x < world_size
        y_in_bound := 0 <= pos.y && pos.y < world_size
        z_in_bound := 0 <= pos.z && pos.z < world_size
        w_in_bound := 0 <= pos.w && pos.w < world_size

        return x_in_bound && y_in_bound && z_in_bound && w_in_bound
    }

    _is_same_pos :: proc(pos1: Pos4D, pos2: Pos4D) -> bool {
        return pos1.x == pos2.x && pos1.y == pos2.y && pos1.z == pos2.z && pos1.w == pos2.w
    }

    for w in pos.w - 1 ..= pos.w + 1 {
        for z in pos.z - 1 ..= pos.z + 1 {
            for y in pos.y - 1 ..= pos.y + 1 {
                for x in pos.x - 1 ..= pos.x + 1 {
                    check_pos := Pos4D{x, y, z, w}
                    if !_is_in_bound(world, check_pos) || _is_same_pos(pos, check_pos) {
                        continue
                    }

                    if world[w][z][y][x] == true {
                        res += 1
                    }
                }
            }
        }
    }

    return res
}

count_active_cells_4d :: proc(world: World4D) -> int {
    res := 0

    for world3d in world {
        for plane in world3d {
            for row in plane {
                for cell in row {
                    if cell == true {
                        res += 1
                    }
                }
            }
        }
    }

    return res
}

simulate_4d :: proc(initial_plane: [][]byte, nb_cycles: int) -> (nb_alive_cells: int) {
    max_world_size := len(initial_plane) + nb_cycles * 2
    world := create_world_4d(max_world_size)
    next_gen := create_world_4d(max_world_size)

    init_world_4d(&world, initial_plane)

    // fmt.printfln("##### Generation %v #####", 0)
    // print_world(world)

    for cycle in 0 ..< nb_cycles {
        for world3d, w in world {
            for plane, z in world3d {
                for row, y in plane {
                    for cell, x in row {
                        nb_neighbor := get_nb_neighbor_4d(world, {x, y, z, w})
                        switch cell {
                            case true: next_gen[w][z][y][x] = nb_neighbor == 2 || nb_neighbor == 3
                            case false: next_gen[w][z][y][x] = nb_neighbor == 3
                        }
                    }
                }
            }
        }

        world, next_gen = next_gen, world

        // fmt.printfln("##### Generation %v #####", cycle + 1)
        // print_world(world)
    }

    return count_active_cells_4d(world)
}

part2 :: proc(grid: [][]byte) -> int {
    return simulate_4d(grid, 6)
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
    fmt.printfln("Part 2: %v", part2(grid))

    free_all(context.temp_allocator)
}
