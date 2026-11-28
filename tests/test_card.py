import pytest
import tomlkit
from hypothesis import given, assume
from hypothesis.strategies import text, characters

from notation.card import Card, FrenchCard


@given(text(min_size=1), text(min_size=1))
def test_init(suit, rank):
    card = Card(suit, rank)
    assert isinstance(card, Card)


@given(text())
def test_init_empty_suit(rank):
    with pytest.raises(ValueError):
        _ = Card('', rank)


@given(text())
def test_init_empty_rank(suit):
    with pytest.raises(ValueError):
        _ = Card(suit, '')


@given(text(min_size=1, alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                            blacklist_characters=('"', "'"))),
       text(min_size=1, alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                            blacklist_characters=('"', "'"))))
def test_dumps(suit, rank):
    card = Card(suit, rank)
    toml_card = card.dumps()
    expected_toml = f'''\
suit = "{suit}"
rank = "{rank}"
'''
    assume(tomlkit.loads(expected_toml))
    assert toml_card == expected_toml


@given(text(min_size=1, alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                            blacklist_characters=('"', "'", '♦', '♣', '♥', '♠'))))
def test_init_french_invalid_suit(suit):
    with pytest.raises(ValueError):
        _ = FrenchCard(suit, 'A')


@given(text(min_size=1, alphabet=characters(whitelist_categories=('L', 'N', 'S'),
                                            blacklist_characters=(
                                                    '"', "'", 'A', '2', '3', '4', '5', '6', '7',
                                                    '8', '9', 'J', 'Q', 'K'))))
def test_init_french_invalid_rank(rank):
    with pytest.raises(ValueError):
        _ = FrenchCard('♦', rank)


@pytest.mark.parametrize("suit", ['♦', '♣', '♥', '♠'])
@pytest.mark.parametrize("rank", ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
def test_french_dumps(suit, rank):
    card = FrenchCard(suit, rank)
    toml_card = card.dumps()
    expected_toml = f'''\
suit = "{suit}"
rank = "{rank}"
'''
    assume(tomlkit.loads(expected_toml))
    assert toml_card == expected_toml
