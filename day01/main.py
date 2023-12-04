def part_one(input):
    total = 0
    for line in input.split("\n"):
        digits = list(get_digits(line))
        total += int(f"{digits[0]}{digits[-1]}")
    return total

def part_two(input):
    total = 0
    for line in input.split("\n"):
        print(line)
        digits = list(get_digits_two(line))
        print(f"{digits[0]}{digits[-1]}")
        total += int(f"{digits[0]}{digits[-1]}")
    return total
        
def get_digits(line):
    for c in line:
        if c.isdigit():
            yield c

def get_digits_two(line):
   replacements = {
       "one": "1", 
       "two": "2",
       "three": "3",
       "four": "4",
       "five": "5",
       "six": "6",
       "seven": "7",
       "eight": "8",
       "nine": "9",
   }
   for i in range(len(line)):
       substring = line[i:]
       if substring[0].isdigit():
           yield substring[0]
       else:
           for t, v in replacements.items():
               if substring.startswith(t):
                   yield v
   

SAMPLE = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

SAMPLE2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

# sample_tot = part_one(SAMPLE)
# print(f"Sample: {sample_tot}")
# sample_tot = part_two(SAMPLE2)
# print(f"Sample: {sample_tot}")
with open('day01/part1.txt', 'r') as file:
    all_lines = file.read()
    tot = part_one(all_lines)
    print(f"Part one: {tot}")
    tot = part_two(all_lines)
    print(f"Part two: {tot}")
