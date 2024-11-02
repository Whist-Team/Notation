import tomlkit
from hypothesis import given, assume, example
from hypothesis.strategies import lists

from notation.card import Card
from notation.stack import Stack
from tests.composites import build_card


@given(lists(build_card()))
@example([Card(suit="Heart", rank="King")])
@example([Card(suit="Heart", rank="King"), Card(suit='♦', rank="K")])
def test_dumps(cards):
    stack = Stack(cards=cards)
    toml_stack: str = stack.dumps()
    stack = (f'[[stack]]\nsuit = "{card.suit}"\nrank = "{card.rank}"\n' for card in cards)
    expected_toml = "\n".join(stack)
    assume(tomlkit.loads(expected_toml))
    assert toml_stack == expected_toml
