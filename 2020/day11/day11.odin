package day11

import "core:fmt"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

count_adjacent_occupied_seats :: proc(grid: [][]u8, base_row: int, base_col: int) -> int {
    res := 0

    nb_rows := len(grid)
    nb_cols := len(grid[0])

    dirs := [?][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}}

    for dir in dirs {
        dx, dy := dir[0], dir[1]
        row, col := base_row + dy, base_col + dx

        if row < 0 || row >= nb_rows || col < 0 || col >= nb_cols {
            continue
        }

        if grid[row][col] == '#' {
            res += 1
        }
    }

    return res
}

count_visible_occupied_seats :: proc(grid: [][]u8, base_row: int, base_col: int) -> int {
    res := 0

    nb_rows := len(grid)
    nb_cols := len(grid[0])

    dirs := [?][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}}

    for dir in dirs {
        dx, dy := dir[0], dir[1]
        row, col := base_row + dy, base_col + dx
        for !(row < 0 || row >= nb_rows || col < 0 || col >= nb_cols) {
            if grid[row][col] == '#' {
                res += 1
                break
            } else if grid[row][col] == 'L' {
                break
            }

            row += dy
            col += dx
        }
    }

    return res
}

part1 :: proc(lines: []string) -> int {
    grid := make([][]u8, len(lines))
    for line, i in lines {
        grid[i] = transmute([]u8)strings.clone(line)
    }

    run_simulation :: proc(grid: [][]u8) {
        grid := grid

        nb_rows := len(grid)
        nb_cols := len(grid[0])

        next_gen := make([][]u8, nb_rows)
        for _, i in next_gen {
            next_gen[i] = make([]u8, nb_cols)
        }

        for {
            changed := false

            for line, row in grid {
                for cell, col in line {
                    switch cell {
                        case 'L':
                            nb_occupied_seats := count_adjacent_occupied_seats(grid, row, col)
                            if nb_occupied_seats == 0 {
                                next_gen[row][col] = '#'
                                changed = true
                            } else {
                                next_gen[row][col] = 'L'
                            }
                        case '#':
                            nb_occupied_seats := count_adjacent_occupied_seats(grid, row, col)
                            if nb_occupied_seats >= 4 {
                                next_gen[row][col] = 'L'
                                changed = true
                            } else {
                                next_gen[row][col] = '#'
                            }
                        case '.': next_gen[row][col] = '.'
                        case: panic("Unknown cell type")
                    }
                }
            }

            grid, next_gen = next_gen, grid

            // fmt.println()
            // for row in grid {
            //     fmt.printfln("%s", string(row))
            // }

            if !changed {
                break
            }
        }
    }

    run_simulation(grid)

    res := 0
    for row in grid {
        for cell in row {
            if cell == '#' {
                res += 1
            }
        }
    }

    return res
}

part2 :: proc(lines: []string) -> int {
    grid := make([][]u8, len(lines))
    for line, i in lines {
        grid[i] = transmute([]u8)strings.clone(line)
    }

    run_simulation :: proc(grid: [][]u8) {
        grid := grid

        nb_rows := len(grid)
        nb_cols := len(grid[0])

        next_gen := make([][]u8, nb_rows)
        for _, i in next_gen {
            next_gen[i] = make([]u8, nb_cols)
        }

        for {
            changed := false

            for line, row in grid {
                for cell, col in line {
                    switch cell {
                        case 'L':
                            nb_occupied_seats := count_visible_occupied_seats(grid, row, col)
                            if nb_occupied_seats == 0 {
                                next_gen[row][col] = '#'
                                changed = true
                            } else {
                                next_gen[row][col] = 'L'
                            }
                        case '#':
                            nb_occupied_seats := count_visible_occupied_seats(grid, row, col)
                            if nb_occupied_seats >= 5 {
                                next_gen[row][col] = 'L'
                                changed = true
                            } else {
                                next_gen[row][col] = '#'
                            }
                        case '.': next_gen[row][col] = '.'
                        case: panic("Unknown cell type")
                    }
                }
            }

            grid, next_gen = next_gen, grid

            // fmt.println()
            // for row in grid {
            //     fmt.printfln("%s", string(row))
            // }

            if !changed {
                break
            }
        }
    }

    run_simulation(grid)

    res := 0
    for row in grid {
        for cell in row {
            if cell == '#' {
                res += 1
            }
        }
    }

    return res
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    // fmt.printfln("%#v", lines)

    fmt.printfln("Part 1: %v", part1(lines))
    fmt.printfln("Part 2: %v", part2(lines))

    free_all(context.temp_allocator)
}
