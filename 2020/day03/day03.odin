package day03

import "core:fmt"
import "core:os"
import "core:strings"


// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(grid: []string) -> int {
	res := 0

	col := 0
	row_len := len(grid[0])
	for row in 0 ..< len(grid) {
		if grid[row][col] == '#' {
			res += 1
		}

		col += 3
		col %= row_len
	}

	return res
}

part2 :: proc(grid: []string) -> int {
	Slope :: struct {
		dx: int,
		dy: int,
	}

	res := 0
	slopes := [5]Slope{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}

	row_len := len(grid[0])
	nb_rows := len(grid)
	for i in 0 ..< 5 {
		col := 0
		slope := slopes[i]
		local_res := 0

		for row := 0; row < nb_rows; row += slope.dy {
			if grid[row][col] == '#' {
				local_res += 1
			}

			col += slope.dx
			col %= row_len
		}

		res = local_res if res == 0 else res * local_res
	}

	return res
}

main :: proc() {
	data, err := os.read_entire_file(INPUT, context.temp_allocator)
	if err != nil {
		fmt.eprintfln("Failed to load the file '%s': %v", INPUT, err)
		os.exit(1)
	}

	file := string(data)
	lines := strings.split_lines(file, context.temp_allocator)

	fmt.print("Part 1: ")
	sol1 := part1(lines)
	fmt.println(sol1)

	fmt.print("Part 2: ")
	sol2 := part2(lines)
	fmt.println(sol2)

	free_all(context.temp_allocator)
}
