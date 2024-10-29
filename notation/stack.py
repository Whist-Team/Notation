"""Implementation of a stack of cards."""
from typing import List

import tomlkit

from notation.card import Card

# pylint: disable=too-few-public-methods
class Stack:
    """A list of cards."""
    def __init__(self, cards: List[Card]):
        self._card_list: List[Card] = cards

    def dumps(self) -> str:
        """Returns the stack as TOML string."""
        card_dump = {'cards': [{'suit': card.suit, 'rank': card.rank} for card in self._card_list]}
        return tomlkit.dumps({'stack': card_dump})
