"""Wrapper for player data."""


# pylint: disable=too-few-public-methods
class Player:
    """Class containing player data."""

    def __init__(self, name: str, team: int, seat: int):
        """Constructs
        :param name: name of player
        :param team: integer of the team ID
        :param seat: The unique identifier of place at table for that player.
        """
        self._name = name
        self._team = team
        self._seat = seat

    def dict(self) -> dict[str, str]:
        """Return player data as dictionary."""
        return {'name': self._name, 'team': self._team, 'seat': self._seat}
