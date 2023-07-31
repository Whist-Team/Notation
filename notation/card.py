import tomli_w


class Card:
    def __init__(self, suit: str, rank: str):
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

    def dumps(self) -> str:
        return tomli_w.dumps({'suit': self._suit, 'rank': self._rank})


class FrenchCard(Card):
    @staticmethod
    def _valid_suit(suit: str) -> str:
        if suit not in ('♦', '♣', '♥', '♠'):
            raise ValueError('Not a correct french suit.')
        return suit

    @staticmethod
    def _valid_rank(rank: str) -> str:
        if rank not in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
            raise ValueError('Not a correct french rank.')
        return rank
