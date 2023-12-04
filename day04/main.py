import re
from util import Source

def part2(input):
    total = 0
    copies = [0]
    for card in input:
        card_copies = 1 + (copies.pop(0) if copies else 0) # 1 for the original
        total += card_copies
        for i in range(count_matches(card)):
            if not i < len(copies):
                copies += [0]
            copies[i] += card_copies
    return total
        

def part1(input):
    return sum(score_card(line) for line in input)

WINNING_NUMBER_RE = r":\s*([0-9\s]+)"
MY_NUMBER_RE = r"\|\s*([0-9\s]+)"
def count_matches(card):
    my_matched = re.findall(MY_NUMBER_RE, card)
    assert my_matched
    my_numbers = my_matched[0].split()

    winning_matched = re.findall(WINNING_NUMBER_RE, card)
    assert winning_matched
    winning_numbers = set(winning_matched[0].split())
    return sum(1 for n in my_numbers if n in winning_numbers)

def score_card(card):
    count = count_matches(card)
    return pow(2, count-1) if count else 0

    


source = Source("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""")
source.filename="day04/input.txt"
# part1_result = part1(source.get_input())
# print(f"Part one: {part1_result}")
part2_result = part2(source.get_input())
print(f"Part two: {part2_result}")
