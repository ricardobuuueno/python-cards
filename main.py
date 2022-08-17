from poker.card import Card
from poker.deck import Deck

card1 = Card(rank = "2", suit = "Spades")
card2 = Card(rank = "Ace", suit = "Hearts")

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

#from main import card1, card2
