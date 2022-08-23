from poker.card import Card
from poker.deck import Deck
from poker.game_round import GameRound
from poker.hand import Hand
from poker.player import Player

card1 = Card(rank = "2", suit = "Spades")
card2 = Card(rank = "Ace", suit = "Hearts")

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name = "Ricardo", hand = hand1)
player2 = Player(name = "Bueno", hand = hand2)
players = [player1, player2]

game_round = GameRound(deck = deck, players = players)
game_round.play()

for player in players:
    print(f"{player.name} receives a {player.hand}")
    index, hand_name, hand_cards = player.best_hand()
    hand_cards_strings = [str(card) for card in hand_cards]
    hand_cards_string = " and ".join(hand_cards_strings)
    print(f"{player.name} has a {hand_name} with a {hand_cards_string}")

winning_player = max(players)

print(f"The winner is {winning_player.name}.")

# print(player1.hand)
# print(player1.best_hand())
# print(player2.hand)
# print(player2.best_hand())


#from main import deck, cards, game_round, hand1, hand2, player1, player2
