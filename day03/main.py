from typing import Dict, List, Tuple
from collections import defaultdict


def part2(input):
    grid = input.split("\n")
    gears: Dict[Tuple[int, int], List[int]] = defaultdict(list)
    for y in range(len(grid)):
        line = grid[y]
        current_number, current_gears = "", set()
        for x in range(len(line) + 1):
            c = line[x] if x < len(line) else ""
            if not c.isdigit():
                if current_number:
                    for gear in current_gears:
                        if gear:
                            gears[gear].append(int(current_number))
                current_number, current_gears = "", set()
            else:
                current_number += c
                for xx in range(x - 1, x + 2):
                    for yy in range(y - 1, y + 2):
                        current_gears.add(check_gear(grid, xx, yy))
    return sum(
        parts[0] * parts[1] 
        for parts in gears.values() 
        if len(parts) == 2
    )


def part1(input):
    total = 0
    grid = input.split("\n")
    for y in range(len(grid)):
        line = grid[y]
        current_number, is_adjacent = "", False
        for x in range(len(line) + 1):
            c = line[x] if x < len(line) else ""
            if not c.isdigit():
                if current_number:
                    # print(f"{current_number} {is_adjacent}")
                    if is_adjacent:
                        total += int(current_number)
                    current_number, is_adjacent = "", False
            else:
                current_number += c
                for xx in range(x - 1, x + 2):
                    for yy in range(y - 1, y + 2):
                        is_adjacent = is_adjacent or check_adjacent(grid, xx, yy)
    return total


def check_gear(grid, x, y):
    if y >= 0 and y < len(grid):
        if x >= 0 and x < len(grid[y]):
            c = grid[y][x]
            if c == "*":
                return (x, y)


def check_adjacent(grid, x, y):
    if y >= 0 and y < len(grid):
        if x >= 0 and x < len(grid[y]):
            c = grid[y][x]
            # print(f"   {c} {x} {y}")
            return not (c.isdigit() or c == ".")
    return False


SAMPLE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

with open("day03/input.txt", "r") as file:
    all_lines = file.read()
r = part1(all_lines)
print(f"part one {r}")
r = part2(all_lines)
print(f"part two {r}")
