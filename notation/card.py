"""Python implementation of a general card and specific versions."""
import tomlkit

FRENCH_SUITS = ('♦', '♣', '♥', '♠')

FRENCH_RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')


class Card:
    """General representation of a card."""

    def __init__(self, suit: str, rank: str) -> None:
        """
        Construct a card.

        :param suit: The suit of the card.
        :param rank: The rank of the card.
        """
        self._suit: str = self._valid_suit(suit)
        self._rank: str = self._valid_rank(rank)

    @staticmethod
    def _valid_suit(suit: str) -> str:
        if not isinstance(suit, str):
            raise ValueError('Suit must be string.')
        if not suit:
            raise ValueError('Suit cannot be empty.')
        return suit

    @staticmethod
    def _valid_rank(rank: str) -> str:
        if not isinstance(rank, str):
            raise ValueError('Rank must be string.')
        if not rank:
            raise ValueError('Rank must not be empty.')
        return rank

    @property
    def suit(self) -> str:
        """Returns the suit of a card as string."""
        return self._suit

    @property
    def rank(self) -> str:
        """Returns the rank of a card as string."""
        return self._rank

    def dumps(self) -> str:
        """Return the card as TOML string."""
        return tomlkit.dumps(self.dict())

    def dict(self):
        """Return the card as dictionary."""
        return {'suit': self._suit, 'rank': self._rank}


class FrenchCard(Card):
    """Represents a French card."""

    @staticmethod
    def _valid_suit(suit: str) -> str:
        if suit not in FRENCH_SUITS:
            raise ValueError('Not a correct french suit.')
        return suit

    @staticmethod
    def _valid_rank(rank: str) -> str:
        if rank not in FRENCH_RANKS:
            raise ValueError('Not a correct french rank.')
        return rank
