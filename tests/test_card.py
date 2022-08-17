import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit  = "Hearts")
        self.assertEqual(card.rank, "Queen")
    
    def test_has_suit(self):
        card = Card(rank = "2", suit  = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_has_string_representation_with_rank_and_suit(self):
        card = Card(rank = "5", suit = "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")

    def test_has_technical_representation(self):
        card = Card("5", "Diamonds")
        self.assertEqual(repr(card), "Card('5', 'Diamonds')")

    def test_card_has_four_suit_options(self):
        self.assertEqual
        (
            Card.SUITS,
            ("Hearts", "Clubs", "Spades", "Diamonds")
        )

    def test_card_has_thirteen_possible_hank_options(self):
        self.assertEqual(
            Card.RANKS,
            (
                "2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"
            )
        )

    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hearts")

    def test_card_only_allows_for_valid_suits(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Dots")

    def test_can_create_standard_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)

        self.assertEqual(
            cards[0],
            Card(rank = "2", suit = "Hearts")
        )

        self.assertEqual(
            cards[-1],
            Card(rank = "Ace", suit = "Diamonds")
        )

    def test_figures_out_if_two_cards_are_equal(self):
        self.assertEqual(
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "2", suit = "Hearts")
        )