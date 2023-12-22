from typing import List
from rich.console import Console
from util import Source

console = Console()


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x, self.y, self.z = x, y, z

    @classmethod
    def from_str(cls, point_string):
        return cls(*map(int, point_string.split(",")))

    def fall(self):
        return Point(self.x, self.y, self.z-1)

    def __repr__(self):
        return f"{self.x},{self.y},{self.z}"


class Brick:
    def __init__(self, start, end):
        self.start, self.end = start, end
        assert self.start.z <= self.end.z
        assert (
            sum(getattr(self.start, attr) == getattr(self.end, attr) for attr in "xyz")
            >= 2
        ), "Bricks are lines"
    @classmethod
    def from_str(cls, line: str):
        return cls(*map(Point.from_str, line.split("~")))

    def try_fall(self, occupied: List["Brick"]):
        try_brick = Brick(self.start.fall(), self.end.fall())
        if try_brick.start.z < 1:
            return self
        for other in occupied:
            if try_brick.intersects(other):
                return self
        return try_brick

    def intersects(self, other) -> bool:
        # Check if one line is to the "left" of the other on the x-axis
        if self.start.x > other.end.x or other.start.x > self.end.x:
            return False
        # Check if one line is "above" the other on the y-axis
        if self.start.y > other.end.y or other.start.y > self.end.y:
            return False
        # Check if one line is "in front of" the other on the z-axis
        if self.start.z > other.end.z or other.start.z > self.end.z:
            return False
        # If all projections overlap, the lines intersect (or are contiguous)
        return True

    def __repr__(self):
        return f"{self.start}~{self.end}"

def progress_bricks(bricks):
    next_bricks = []
    for brick in bricks:
        next_bricks.append(brick.try_fall(next_bricks))
    return next_bricks

def part2(lines):
    bricks = [Brick.from_str(line) for line in lines]
    bricks.sort(key=lambda brick: brick.start.z)
    while True:
        next_bricks = progress_bricks(bricks)
        if next_bricks == bricks:
            break
        bricks = next_bricks

    console.print("finished falling")
    count = 0
    for i in range(len(bricks)):
        permuted = bricks[:i] + bricks[i+1:]
        possible = progress_bricks(permuted)
        different = sum(1 for x, y in zip(permuted, possible) if x != y)
        count += different
        if i % 20 == 0:
            console.print(f"{i} of {len(bricks)}")

    return count



source = Source(
    """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""",
    "day22/input.txt",
)
result = part2(source.get_input())
console.print(f":two: {result}")
