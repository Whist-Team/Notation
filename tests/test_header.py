import string
from datetime import datetime

import pytest
import tomlkit
from hypothesis import assume, example, given
from hypothesis.strategies import datetimes, lists, integers, composite, text, builds, uuids

from notation.header import Header
from notation.player import Player
from tests.composites import build_player, build_player_list


@composite
def build_header_dumps(draw):
    timestamp = draw(datetimes())
    amount_players = draw(integers(min_value=1, max_value=10))
    players = draw(lists(builds(Player, name=text(alphabet=string.ascii_letters, min_size=1),
                                team=integers(), seat=integers()),
                         min_size=1,
                         max_size=amount_players,
                         unique=True))
    teams = draw(integers(max_value=len(players)))
    return (timestamp, players, teams)


@given(build_header_dumps())
@example((datetime.now(), [Player(name='John', team=1, seat=0)], 1))
@example((datetime.now(), [Player(name='John', team=1, seat=0),
                           Player(name='John', team=1, seat=1)], 1))
def test_dumps(data):
    start_time, players, number_teams = data
    header = Header(start_time=start_time, players=players, number_teams=number_teams)
    header_dump = header.dumps()
    player_string = ((f'[[players]]\n'
                      f'name = "{player._name}"\n'
                      f'team = {player._team}\n'
                      f'seat = {player._seat}') for player in players)
    expected_toml = (f'[header]\ntimestamp = "{start_time.isoformat()}"\nnumber_of_teams = '
                     f'{number_teams}\n\n')
    expected_toml += "\n\n".join(player_string) + '\n'
    assume(tomlkit.loads(expected_toml))
    assert header_dump == expected_toml


@given(build_header_dumps(), text(alphabet=string.ascii_letters, min_size=1))
@example((datetime.now(), [Player(name='John', team=1, seat=0)], 1), 'Europe')
def test_dumps_with_location(data, location):
    start_time, players, number_teams = data
    header = Header(start_time=start_time, players=players, number_teams=number_teams,
                    location=location)
    header_dump = header.dumps()
    player_string = ((f'[[players]]\n'
                      f'name = "{player._name}"\n'
                      f'team = {player._team}\n'
                      f'seat = {player._seat}') for player in players)
    expected_toml = (f'[header]\ntimestamp = "{start_time.isoformat()}"\nnumber_of_teams = '
                     f'{number_teams}\nlocation = "{location}"\n\n')
    expected_toml += "\n\n".join(player_string) + '\n'
    assume(tomlkit.loads(expected_toml))
    assert header_dump == expected_toml


def test_empty_player_list():
    with pytest.raises(ValueError):
        Header(start_time=datetime.now(), players=[], number_teams=1)


def test_more_teams_than_players():
    with pytest.raises(ValueError):
        Header(start_time=datetime.now(), players=[Player(name='John', team=1, seat=0)],
               number_teams=2)
