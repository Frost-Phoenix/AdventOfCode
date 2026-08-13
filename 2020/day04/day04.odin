package day04

import "core:fmt"
import "core:slice"
import "core:strconv"
import "core:strings"


// INPUT :: "test.txt"
INPUT :: "input.txt"

is_valid_year :: proc(value: string, low: int, high: int) -> bool {
    if len(value) != 4 {
        return false
    }

    year := strconv.parse_int(value, 10) or_return

    if year < low || year > high {
        return false
    }

    return true
}

is_valid_height :: proc(value: string) -> bool {
    if strings.ends_with(value, "cm") {
        height := strconv.parse_int(value[:len(value) - 2], 10) or_return

        if height < 150 || height > 193 {
            return false
        }
    } else if strings.ends_with(value, "in") {
        height := strconv.parse_int(value[:len(value) - 2], 10) or_return

        if height < 59 || height > 76 {
            return false
        }
    } else {
        return false
    }

    return true
}

is_valid_ecl :: proc(value: string) -> bool {
    return slice.contains([]string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}, value)
}

is_valid_hcl :: proc(value: string) -> bool {
    if len(value) != 7 || value[0] != '#' {
        return false
    }

    for c in value[1:] {
        if !(('0' <= c && c <= '9') || ('a' <= c && c <= 'f')) {
            return false
        }
    }

    return true
}

is_valid_pid :: proc(value: string) -> bool {
    _, is_integer := strconv.parse_int(value, 10)
    return len(value) == 9 && is_integer
}

is_valid_passport :: proc(fields: []string, validate_fields_values: bool) -> bool {
    if len(fields) < 7 {
        return false
    }

    if validate_fields_values {
        for filed in fields {
            prefix := filed[:3]
            value := filed[4:]

            switch prefix {
                case "byr": is_valid_year(value, 1920, 2002) or_return
                case "iyr": is_valid_year(value, 2010, 2020) or_return
                case "eyr": is_valid_year(value, 2020, 2030) or_return
                case "hgt": is_valid_height(value) or_return
                case "hcl": is_valid_hcl(value) or_return
                case "pid": is_valid_pid(value) or_return
                case "ecl": is_valid_ecl(value) or_return
            }
        }
    }

    if len(fields) == 7 {
        for field in fields {
            if strings.starts_with(field, "cid:") {
                return false
            }
        }
    }

    return true
}

part1 :: proc(passports: []string) -> int {
    res := 0

    for passport in passports {
        fields := strings.split_multi(passport, {" ", "\n"})

        if is_valid_passport(fields, false) {
            res += 1
        }
    }

    return res
}

part2 :: proc(passports: []string) -> int {
    res := 0

    for passport in passports {
        fields := strings.split_multi(passport, {" ", "\n"})

        if is_valid_passport(fields, true) {
            res += 1
        }
    }

    return res
}

main :: proc() {
    context.allocator = context.temp_allocator

    data := #load(INPUT)
    file := string(data)
    passports := strings.split(file, "\n\n")

    fmt.printfln("Part 1: %v", part1(passports))
    fmt.printfln("Part 2: %v", part2(passports))

    free_all(context.temp_allocator)
}
