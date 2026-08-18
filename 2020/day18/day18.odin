package day18

import "core:fmt"
import "core:strings"

// INPUT :: "test.txt"
INPUT :: "input.txt"

Token_Type :: enum {
    Val,
    Add,
    Mull,
    LPar,
    RPar,
}

Token :: struct {
    type:  Token_Type,
    value: int,
}

parse_expression :: proc(expr: string) -> []Token {
    tokens := make([dynamic]Token)

    for c in expr {
        switch c {
            case ' ': continue
            case '+': append(&tokens, Token{.Add, 0})
            case '*': append(&tokens, Token{.Mull, 0})
            case '(': append(&tokens, Token{.LPar, 0})
            case ')': append(&tokens, Token{.RPar, 0})
            case: append(&tokens, Token{.Val, int(c) - '0'})
        }
    }

    return tokens[:]
}

evaluate_expression_no_precedence :: proc(tokens: []Token) -> (acc: int, idx: int) {
    acc = 0
    opperator: Token_Type = nil

    _add_value :: proc(acc: ^int, opperator: Token_Type, val: int) {
        if opperator == nil {
            acc^ = val
            return
        }

        #partial switch opperator {
            case .Add: acc^ += val
            case .Mull: acc^ *= val
        }
    }

    i := 0
    for ; i < len(tokens); i += 1 {
        token := tokens[i]

        switch token.type {
            case .Val: _add_value(&acc, opperator, token.value)
            case .Add, .Mull: opperator = token.type
            case .LPar:
                val, offset := evaluate_expression_no_precedence(tokens[i + 1:])
                i += offset + 1
                _add_value(&acc, opperator, val)
            case .RPar: return acc, i
        }
    }

    return acc, i
}

evaluate_expression_plus_precedence :: proc(tokens: []Token) -> (acc: int, idx: int) {
    product := 1
    sum := 0

    i := 0
    for ; i < len(tokens); i += 1 {
        token := tokens[i]

        switch token.type {
            case .Val: sum += token.value
            case .Add:
            case .Mull:
                product *= sum
                sum = 0
            case .LPar:
                val, offset := evaluate_expression_plus_precedence(tokens[i + 1:])
                i += offset + 1
                sum += val
            case .RPar:
                product *= sum
                return product, i
        }
    }

    product *= sum

    return product, i
}

part1 :: proc(lines: []string) -> int {
    res := 0

    for line in lines {
        tokens := parse_expression(line)
        acc, _ := evaluate_expression_no_precedence(tokens)

        // fmt.println(acc)

        res += acc
    }

    return res
}

part2 :: proc(lines: []string) -> int {
    res := 0

    for line in lines {
        tokens := parse_expression(line)
        acc, _ := evaluate_expression_plus_precedence(tokens)

        // fmt.println(acc)

        res += acc
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
