from datetime import datetime
from typing import List, Optional

import tomlkit

from notation.player import Player


class Header:
    def __init__(self, start_time: datetime, players: List[Player],
                 number_teams: int, location: Optional[str] = None, ):
        self._start_time: datetime = start_time
        self._location = location
        self._players = players
        self._number_teams = number_teams

    def dumps(self) -> str:
        players = {f'seat_{index}':
                       [{'name': player._name,
                         'team': player._team}] for index, player in enumerate(self._players)}
        header_dump = {'header': {'timestamp': self._start_time.isoformat(),
                                  'number_of_teams': self._number_teams},
                       'players': players}
        return tomlkit.dumps(header_dump)
