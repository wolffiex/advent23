from dataclasses import dataclass
from enum import IntEnum, auto
from functools import total_ordering
from rich.console import Console
from util import Source
from collections import Counter

class HandType(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_KIND = auto()
    FIVE_KIND = auto()

@total_ordering
@dataclass
class Hand:
    cards: str
    bid: int

    @classmethod
    def from_line(cls, line):
        cards, bid_str = line.split()
        return cls(cards, int(bid_str))

    def get_type(self):
        freq = dict(Counter(self.cards))
        if 'J' in freq:
            js = freq.pop('J')
            if not freq:
                freq['A'] = 0
            max_card = max(freq, key=freq.get)
            freq[max_card] += js
        if len(freq.keys()) == 5:
            return HandType.HIGH_CARD
        elif len(freq.keys()) == 4:
            return HandType.ONE_PAIR
        elif len(freq.keys()) == 3:
            return (
                HandType.THREE_KIND
                if any(value == 3 for value in freq.values()) else
                HandType.TWO_PAIR
            )
        elif len(freq.keys()) == 2:
            return (
                HandType.FOUR_KIND
                if any(value == 4 for value in freq.values()) else
                HandType.FULL_HOUSE
            )
        else:
            assert len(freq.keys()) == 1
            return HandType.FIVE_KIND

    def __lt__(self, other):
        if self.get_type() != other.get_type():
            return self.get_type() < other.get_type()
        else:
            # If types are equal, proceed to card comparison
            return self.cards_lt(other.cards)

    CARD_ORDER = "AKQT98765432J"
    def cards_lt(self, other_cards):
        for i in range(len(self.cards)):
            self_card_rank = self.CARD_ORDER.index(self.cards[i])
            other_card_rank = self.CARD_ORDER.index(other_cards[i])
            if self_card_rank == other_card_rank:
                continue
            return self_card_rank > other_card_rank



def part_two(input_):
    hands = [Hand.from_line(l) for l in input_]
    hands.sort()
    return sum(
        hand.bid * i
        for i, hand in enumerate(hands, 1)
    )

source = Source("""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""", "day07/input.txt") 

console = Console()
result1 = part_two(source.get_input())
console.print(f":two: sample {result1}")
