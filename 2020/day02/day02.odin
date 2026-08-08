package day02

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strconv/decimal"
import "core:strings"


// INPUT :: "test.txt"
INPUT :: "input.txt"

part1 :: proc(lines: []string) {
	res := 0
	for l in lines {
		split := strings.split_multi(l, {"-", " ", ": "}, context.temp_allocator) or_continue

		min := strconv.parse_int(split[0], 10) or_continue
		max := strconv.parse_int(split[1], 10) or_continue
		letter := split[2]
		password := split[3]

		count := strings.count(password, letter)

		if min <= count && count <= max {
			res += 1
		}
	}

	fmt.println(res)
}

part2 :: proc(lines: []string) {
	res := 0
	for l in lines {
		split := strings.split_multi(l, {"-", " ", ": "}, context.temp_allocator) or_continue

		p1 := (strconv.parse_int(split[0], 10) or_continue) - 1
		p2 := (strconv.parse_int(split[1], 10) or_continue) - 1
		letter := split[2][0]
		password := split[3]

		if (password[p1] == letter || password[p2] == letter) && password[p1] != password[p2] {
			res += 1
		}
	}

	fmt.println(res)
}

main :: proc() {
	data, err := os.read_entire_file(INPUT, context.temp_allocator)
	if err != nil {
		fmt.eprintfln("Failed to load the file '%s': %v", INPUT, err)
		os.exit(1)
	}

	file := string(data)
	lines := strings.split_lines(file, context.temp_allocator)

	part1(lines)
	part2(lines)

	free_all(context.temp_allocator)
}
