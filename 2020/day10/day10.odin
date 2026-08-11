package day10

import "core:fmt"
import "core:slice"
import "core:strconv"
import "core:strings"

// INPUT :: "test1.txt"
// INPUT :: "test2.txt"
INPUT :: "input.txt"

part1 :: proc(numbers: []int) -> int {
    slice.sort(numbers)

    last := 0
    diffs: [3]int // an array, so diff of 1 is index 0 and diff of 3 is index 2

    for v, i in numbers {
        diffs[v - last - 1] += 1
        last = v
    }

    diffs[2] += 1 // diff between last adaptater and built-in

    return diffs[0] * diffs[2]
}

part2 :: proc(numbers: []int) -> int {
    slice.sort(numbers)

    Cache_Entry :: struct {
        numbers_len: int,
        last:        int,
    }
    cache := make(map[Cache_Entry]int)

    get_nb_combinations :: proc(numbers: []int, last: int, cache: ^map[Cache_Entry]int) -> int {
        cache_entry := Cache_Entry{len(numbers), last}
        cached_value, cache_exist := cache[cache_entry]

        if cache_exist {
            return cached_value
        }

        if (len(numbers) == 1 || len(numbers) == 0) {
            return 1
        }

        total := 0
        for i in 0 ..< 3 {
            if i >= len(numbers) || numbers[i] > last + 3 {
                break
            }

            total += get_nb_combinations(numbers[i + 1:], numbers[i], cache)
        }

        cache[{len(numbers), last}] = total

        return total
    }

    return get_nb_combinations(numbers, 0, &cache)
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    lines := strings.split_lines(file)

    numbers := make([dynamic]int, 0, len(lines))
    for line in lines {
        n, _ := strconv.parse_int(line, 10)
        append(&numbers, n)
    }

    // fmt.println(numbers[:])

    fmt.printfln("Part 1: %v", part1(numbers[:]))
    fmt.printfln("Part 2: %v", part2(numbers[:]))

    free_all(context.temp_allocator)
}
