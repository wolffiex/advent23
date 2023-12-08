import re
from rich.console import Console
import math
from functools import reduce

from util import Source

console = Console()

NODE_RE = r"(\w+) = \((\w+), (\w+)\)"


def get_node(line):
    match = re.search(NODE_RE, line)
    assert match
    return match.group(1), (match.group(2), match.group(3))


def part1(lines):
    instructions = next(lines)
    assert not next(lines)  # empty
    nodes = {name: edges for name, edges in (get_node(line) for line in lines)}
    ghosts = [name for name in nodes.keys() if name.endswith('A')]
    gzs = [[] for _ in range(len(ghosts))]
    c = 0
    steps = 0
    while True:
        direction = instructions[c]
        next_node = lambda node: node[0] if direction == 'L' else node[1]
        ghosts = [*map(next_node, (nodes[ghost] for ghost in ghosts))]
        for i, g in enumerate(ghosts):
            if (g.endswith("Z")):
                gzs[i].append(steps)
        c += 1
        c %= len(instructions)
        steps += 1
        if all(len(gz) > 2 for gz in gzs):
            differences = [gz[1] - gz[0] for gz in gzs]
            return math.lcm(*differences)


source = Source( """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""", "day08/input.txt")
result = part1(source.get_input())
console.print(f":two: {result}")
