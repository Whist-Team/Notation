from typing import List

import tomlkit

from notation.card import Card


class Stack:
    def __init__(self, cards: List[Card]):
        self._card_list: List[Card] = cards

    def dumps(self) -> str:
        card_dump = {'cards': [{'suit': card.suit, 'rank': card.rank} for card in self._card_list]}
        return tomlkit.dumps({'stack': card_dump})
