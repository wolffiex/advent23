from rich.console import Console
from util import Source

console = Console()
def main(input_):
    for line in input_:
        starting_row = [*map(int, line.split())]
        rows = [starting_row]
        while not all(x == 0 for x in rows[-1]):
            rows.append([*row_difference(rows[-1])])
        rows.reverse()
        for i in range(0, len(rows)):
            rows[i].append(0 if i == 0 else rows[i][-1] + rows[i-1][-1])
        yield rows[-1][-1]

def row_difference(row):
    for i in range(1, len(row)):
        yield row[i] - row[i-1]

source = Source(
"""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""",
    "day09/input.txt",
)
result = sum(main(source.get_input()))
console.print(f"Part :one: {result}")
