class Player:
    def __init__(self, name: str, team: int):
        self._name = name
        self._team = team

    def dict(self) -> dict[str, str]:
        return {'name': self._name, 'team': self._team}
