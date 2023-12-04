import math

def run(input):
    total = 0
    for line in input.split("\n"):
        if not line:
            continue
        total += game_value_two(line)
    return total

def game_value_one(line):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    print (line)
    game, rest = line.split(":")
    rounds = (rest.split(";"))
    _, game_num = game.split(" ")
    for game_round in rounds:
        cubes = game_round.split(",")
        for cube in cubes:
            count, color = cube.strip().split(" ")
            print(f"{count}:{color}")
            if max_cubes[color] < int(count):
                return 0
    return int(game_num)
    
def game_value_two(line):
    game, rest = line.split(":")
    rounds = (rest.split(";"))
    min_cubes = {"red":0, "green":0, "blue":0}
    for game_round in rounds:
        cubes = game_round.split(",")
        for cube in cubes:
            count, color = cube.strip().split(" ")
            min_cubes[color] = max(min_cubes[color], int(count))
    return math.prod(min_cubes.values())


SAMPLE_ONE = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

with open('day02/input.txt', 'r') as file:
    all_lines = file.read()
total = run(all_lines)
print(f"part two: {total}")
