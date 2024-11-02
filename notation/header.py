"""Header containing the meta data of a game."""
from datetime import datetime
from typing import Optional

import tomlkit

from notation.player import Player


# pylint: disable=too-few-public-methods
class Header:
    """Class implementation of a meta data wrapper."""

    def __init__(self, start_time: datetime, players: list[Player],
                 number_teams: int, location: Optional[str] = None, ):
        """Constructor.
        :param start_time: The start time of the game as datetime object
        :param players: The list of players.
        :param number_teams: The number of teams.
        :param location: Optional. Where the game to place.
        """
        self._start_time: datetime = start_time
        self._location = location
        if players is None or len(players) == 0:
            raise ValueError('Player list cannot be empty')
        if number_teams > len(players):
            raise ValueError('Number teams cannot be greater than amount of players')
        self._players = players
        self._number_teams = number_teams

    def dumps(self) -> str:
        """Return a TOML string representation of the header."""
        players = [tomlkit.dumps({'players': [player.dict()]}) for player in self._players]
        header_dump = {'header': {'timestamp': self._start_time.isoformat(),
                                  'number_of_teams': self._number_teams}}
        if self._location:
            header_dump['header']['location'] = self._location
        return f'{tomlkit.dumps(header_dump)}\n{"\n".join(players)}'
