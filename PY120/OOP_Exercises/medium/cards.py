from random import shuffle

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def value(self):
        match self.rank:
            case 'Ace':
                return 14
            case 'King':
                return 13
            case 'Queen':
                return 12
            case 'Jack':
                return 11
            case _:
                return self.rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value() == other.value()
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, Card):
            return self.value() != other.value()
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value() < other.value()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Card):
            return self.value() <= other.value()
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value() > other.value()
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Card):
            return self.value() >= other.value()
        return NotImplemented
     
class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    @classmethod
    def get_shuffled_cards(cls):
        card_list = [Card(rank, suit) for rank in cls.RANKS for suit in cls.SUITS]
        shuffle(card_list)
        return card_list
    
    def __init__(self):
        self.deck = Deck.get_shuffled_cards()

    @property
    def deck(self):
        return self._deck
    
    @deck.setter
    def deck(self, new_deck):
        self._deck = new_deck

    def draw(self):
        drawn_card = self.deck.pop()
        if not self.deck:
            self.deck = Deck.get_shuffled_cards()
        return drawn_card
    
# Include Card and Deck classes from the last two exercises.
class PokerHand:
    def __init__(self, deck):
        self.deck = deck
        self.hand = [self.deck.draw() for _ in range(5)]

    def print(self):
        for card in self.hand:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _value_counts(self):
        values = [card.value() for card in self.hand]
        return {val:values.count(val) for val in set(values)}

    def _is_royal_flush(self):
        return max([card.value() for card in self.hand]) == 14 and self._is_straight_flush()

    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self):
        return max(self._value_counts().values()) == 4

    def _is_full_house(self):
        return sorted(self._value_counts().values()) == [2,3]

    def _is_flush(self):
        return len({card.suit for card in self.hand}) == 1

    def _is_straight(self):
        values = {card.value() for card in self.hand}
        return (max(values) - min(values) == 4) and (len(values) == 5)

    def _is_three_of_a_kind(self):
        return sorted(self._value_counts().values()) == [1,1,3]

    def _is_two_pair(self):
        return sorted(self._value_counts().values()) == [1,2,2]

    def _is_pair(self):
        return sorted(self._value_counts().values()) == [1,1,1,2]


hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")
