from hypothesis.strategies import composite, text, characters, integers

from notation.card import Card
from notation.player import Player


@composite
def build_card(draw):
    suit: str = draw(text(min_size=1, max_size=1,
                          alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                              blacklist_characters=('"', "'"))))
    rank: str = draw(text(min_size=1, max_size=1,
                          alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                              blacklist_characters=('"', "'"))))
    return Card(suit=suit, rank=rank)


@composite
def build_player(draw):
    name = draw(text(alphabet=characters()))
    team = draw(integers())
    return Player(name, team)
