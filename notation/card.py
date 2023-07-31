import tomli_w


class Card:
    def __init__(self, suit: str, rank: str):
        self._suit: str = suit
        self._rank: str = rank

    def dumps(self) -> str:
        return tomli_w.dumps({'suit': self._suit, 'rank': self._rank})


class FrenchCard(Card):
    def __init__(self, suit: str, rank: str):
        super().__init__(self._valid_suit(suit), self._valid_rank(rank))

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
