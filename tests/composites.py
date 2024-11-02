"""Build funtions for hypothesis tests."""
import string

from hypothesis.strategies import composite, text, characters, integers

from notation.card import Card
from notation.player import Player


@composite
def build_card(draw):
    """Build a card with random strings of size one for suit and rank."""
    suit: str = draw(text(min_size=1, max_size=1,
                          alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                              blacklist_characters=('"', "'"))))
    rank: str = draw(text(min_size=1, max_size=1,
                          alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                              blacklist_characters=('"', "'"))))
    return Card(suit=suit, rank=rank)


@composite
def build_player(draw, seat: int):
    """Build a player with random strings of at least size one for the name."""
    name = draw(text(alphabet=string.ascii_letters, min_size=1))
    team = draw(integers())
    return Player(name, team, seat)


@composite
def build_player_list(draw):
    amount_players = draw(integers(min_value=1, max_value=10))
    return [build_player(seat=seat) for seat in range(amount_players)]
