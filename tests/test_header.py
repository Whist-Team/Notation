from datetime import datetime

import pytest
import tomlkit
from hypothesis import assume, example, given
from hypothesis.strategies import datetimes, lists, integers, composite

from notation.header import Header
from notation.player import Player
from tests.composites import build_player


@composite
def build_header_dumps(draw):
    timestamp = draw(datetimes())
    players = draw(lists(build_player(), min_size=1))
    teams = draw(integers(max_value=len(players)))
    return (timestamp, players, teams)


@given(build_header_dumps())
@example((datetime.now(), [Player(name='John', team=1)], 1))
def test_dumps(data):
    start_time, players, number_teams = data
    header = Header(start_time=start_time, players=players, number_teams=number_teams)
    header_dump = header.dumps()
    player_string = ((f'[[players.seat_{index}]]\n'
                      f'name = "{player._name}"\n'
                      f'team = {player._team}') for index, player in enumerate(players))
    expected_toml = (f'[header]\ntimestamp = "{start_time.isoformat()}"\nnumber_of_teams = '
                     f'{number_teams}\n\n')
    expected_toml += "\n\n".join(player_string) + '\n'
    assume(tomlkit.loads(expected_toml))
    assert header_dump == expected_toml


def test_empty_player_list():
    with pytest.raises(ValueError):
        Header(start_time=datetime.now(), players=[], number_teams=1)


def test_more_teams_than_players():
    with pytest.raises(ValueError):
        Header(start_time=datetime.now(), players=[Player(name='John', team=1)], number_teams=2)
