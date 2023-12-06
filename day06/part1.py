from rich.console import Console
from util import Source

console = Console()

def part1(input):
    times = map(int, next(input).split(":")[1].split())
    distances = map(int, next(input).split(":")[1].split())
    console.print(f"f {times}")
    win_product = 1
    for total_time, distance_record in zip(times, distances):
        winning_ways = 0
        console.print(f"race {total_time} {distance_record}")
        for t in range(total_time):
            if calc_distance(t, total_time) > distance_record:
                winning_ways += 1
        win_product *= winning_ways
    return win_product


def calc_distance(t, total_time):
    # console.print(f"{t} {(total_time-t) * t}")
    return (total_time-t) * t



source = Source("""Time:      7  15   30
Distance:  9  40  200""", "day06/input.txt") 

result1_sample = part1(source.get_sample())
console.print(f":one: sample {result1_sample}")
result1_sample = part1(source.get_input())
console.print(f":one: input {result1_sample}")
