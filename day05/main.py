from collections import namedtuple
from dataclasses import dataclass
from typing import List, Optional, Tuple
from util import Source
from rich.console import Console
from itertools import chain

# Create a console object
console = Console()

@dataclass
class SeedRange:
    start: int
    end: int

    def is_valid(self):
        return self.start < self.end

@dataclass
class RangeMap:
    dest_start: int
    src_start: int
    length: int

    @classmethod
    def from_string(cls, line):
        values = [int(value) for value in line.split()]
        return RangeMap(*values)


Map2 = List[RangeMap]
def part_two(input):
    seed_line = next(input)
    assert seed_line.startswith("seeds: ")
    seeds = [int(value) for value in seed_line[len("seeds: "):].split()]
    maps = get_maps2(input)
    lowest = None
    while seeds:
        seed_start, seed_length = seeds[:2]
        seeds = seeds[2:]
        unmapped : List[SeedRange]= [SeedRange(seed_start, seed_start + seed_length -1)]
        mapped = []
        for m in maps:
            for range_map in m:
                if unmapped:
                    result = [apply_range_map(sr, range_map) for sr in unmapped]
                    unmapped_tuple, mapped_tuple = [*zip(*result)]
                    unmapped = [*chain(*unmapped_tuple)]
                    mapped.extend(chain(*mapped_tuple))
            unmapped += mapped
            mapped = []
        for sr in unmapped:
            if not lowest or lowest > sr.start:
                lowest = sr.start
    return lowest
                

def apply_range_map(seed_range:SeedRange, range_map:RangeMap) -> Tuple[List[SeedRange], List[SeedRange]]:
    range_end = range_map.src_start + range_map.length
    mapped = [SeedRange(range_map.src_start, range_end)]
    unmapped = [SeedRange(seed_range.start, range_map.src_start), SeedRange(range_end, seed_range.end)]
    def clip_ranges(ranges):
        for sr in ranges:
            sr.start = max(seed_range.start, sr.start)
            sr.end = min(seed_range.end, sr.end)
        return [*filter(lambda sr: sr.is_valid(), ranges)]
    mapped = clip_ranges(mapped)
    if mapped:
        offset = range_map.dest_start - range_map.src_start
        mapped[0].start += offset
        mapped[0].end += offset


    return clip_ranges(unmapped), mapped


def get_maps2(input):
    maps : List[Map2] = []
    current_map : Map2 = []
    for line in input:
        if not line.strip():
            continue
        elif line.endswith("map:"):
            current_map = []
            maps.append(current_map)
        else:
            current_map.append(RangeMap.from_string(line))
    return maps



MapRange = namedtuple('MapRange', ['dest_start', 'src_start', 'length'])
Map = List[MapRange]
def part_one(input):
    seed_line = next(input)
    assert seed_line.startswith("seeds: ")
    seeds = [int(value) for value in seed_line[len("seeds: "):].split()]
    maps = get_maps(input)
    console.print(maps)
    min_seed = None
    for seed in seeds:
        output = apply_maps(seed, maps)
        if not min_seed or output < min_seed:
            min_seed= output
        console.print(f"{seed} : {output}")
    return min_seed

def get_maps(input):
    maps : List[Map] = []
    current_map : Map = []
    for line in input:
        if not line.strip():
            print('skip')
            continue
        elif line.endswith("map:"):
            current_map = []
            maps.append(current_map)
        else:
            # console.print(line.split())
            current_map.append(MapRange(*(int(value) for value in line.split())))
    return maps

def apply_maps(seed, maps):
    value = seed
    for m in maps:
        # print(f"Apply {value} {m}")
        mapped_value = None
        for map_range in m:
            offset = value - map_range.src_start
            if offset >=0 and offset < map_range.length:
                mapped_value = map_range.dest_start + offset
                # print(f"mmmmm {mapped_value}")
                break

        value = mapped_value or value
    return value



source = Source("""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""", "day05/input.txt")


with open("day05/input.txt", "r") as file:
    all_lines = file.read()
# result1 = part_one(iter(all_lines.split("\n")))
result2 = part_two(iter(all_lines.split("\n")))
# result2 = part_two(source.get_sample())
console.print(f":two: {result2}")
