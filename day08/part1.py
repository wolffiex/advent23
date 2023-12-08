import re
from rich.console import Console

from util import Source

console = Console()

NODE_RE = r"(\w+) = \((\w+), (\w+)\)"


def get_node(line):
    console.print(f"match {line}")
    match = re.search(NODE_RE, line)
    assert match
    return match.group(1), (match.group(2), match.group(3))


def part1(lines):
    instructions = next(lines)
    print(instructions)
    assert not next(lines)  # empty
    nodes = {name: edges for name, edges in (get_node(line) for line in lines)}
    p = "AAA"
    c = 0
    steps = 0
    while p != "ZZZ":
        direction = instructions[c]
        p = nodes[p][0] if direction == 'L' else nodes[p][1]
        c += 1
        c %= len(instructions)
        console.print(f"S {c} {direction} {p}")
        steps += 1
    return steps


source = Source(
    """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""",
    "day08/input.txt",
)
result = part1(source.get_input())
console.print(f":one: {result}")
