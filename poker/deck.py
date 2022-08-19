import random
class Deck():
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_cards(self, number):
        cards_to_remove = self.cards[0:number]
        del self.cards[0:number]
        return cards_to_remove

    def shuffle(self):
        random.shuffle(self.cards)
