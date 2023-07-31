import pytest
from hypothesis import given, example
from hypothesis.strategies import text

from notation.card import Card


@given(text(min_size=1), text(min_size=1))
def test_dumps(suit, rank):
  card = Card(suit, rank)
  assert isinstance(card, Card)

@given(text())
def test_dumps_empty_suit(rank):
  with pytest.raises(ValueError):
    _ = Card('', rank)

@given(text())
def test_dumps_empty_rank(suit):
  with pytest.raises(ValueError):
    _ = Card(suit, '')