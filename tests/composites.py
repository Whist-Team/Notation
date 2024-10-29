from hypothesis import assume
from hypothesis.strategies import composite, text, characters

from notation.card import Card


@composite
def build_card(draw):
    suit: str = draw(text(min_size=1, max_size=1,
                          alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                              blacklist_characters=('"', "'"))))
    rank: str = draw(text(min_size=1, max_size=1,
                          alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                              blacklist_characters=('"', "'"))))
    return Card(suit=suit, rank=rank)
