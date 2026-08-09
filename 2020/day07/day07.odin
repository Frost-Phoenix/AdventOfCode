package day07

import "core:fmt"
import "core:strconv"
import "core:strings"

// INPUT :: "test1.txt"
// INPUT :: "test2.txt"
INPUT :: "input.txt"

Bag_Name :: string
Bag_List :: [dynamic]Bag_Name

Graph :: map[Bag_Name]Bag_List

Rule :: struct {
    bag:             Bag_Name,
    contain_names:   [dynamic]string,
    contain_numbers: [dynamic]int,
}

parse_rule :: proc(rule_sentence: string) -> Rule {
    rule: Rule

    split := strings.split(rule_sentence, " bags contain ")
    rule.bag = split[0]

    for bag in strings.split(split[1][:len(split[1]) - 1], ", ") {
        bag_split := strings.split(bag, " ")
        nb := strconv.parse_int(bag_split[0], 10) or_continue
        name := strings.join(bag_split[1:3], " ")

        append(&rule.contain_names, name)
        append(&rule.contain_numbers, nb)
    }

    return rule
}

part1 :: proc(lines: []string) -> int {
    graph: Graph

    for line in lines {
        rule := parse_rule(line)

        for name in rule.contain_names {
            if name not_in graph {
                graph[name] = make(Bag_List)
            }

            append(&graph[name], rule.bag)
        }
    }

    // fmt.printfln("%#v", graph)

    count :: proc(graph: ^Graph, name: string, counted: ^map[string]bool) -> int {
        if name not_in graph {
            return 0
        }

        res := 0

        for bag in graph[name] {
            if bag in counted {
                continue
            }

            counted[bag] = true
            res += 1 + count(graph, bag, counted)
        }

        return res
    }

    counted: map[string]bool

    return count(&graph, "shiny gold", &counted)
}

part2 :: proc(lines: []string) -> int {
    graph: Graph

    for line in lines {
        rule := parse_rule(line)
        bag := rule.bag

        if bag not_in graph {
            graph[bag] = make(Bag_List)
        }

        for name, i in rule.contain_names {
            for _ in 0 ..< rule.contain_numbers[i] {
                append(&graph[bag], name)
            }
        }
    }

    // fmt.printfln("%#v", graph)

    count :: proc(graph: ^Graph, name: string) -> int {
        if name not_in graph {
            return 0
        }

        res := 0

        for bag in graph[name] {
            res += 1 + count(graph, bag)
        }

        return res
    }

    return count(&graph, "shiny gold")
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
