Card Game Notation Standard
===========================
This standard uses TOML_ as notation language.

Header
-------
All meta data is defined in the Header.
This contains information about teams and players.
Furthermore, the location and datetime is stated.

.. code-block:: toml

    [header]
    # Timestamp of the starting time in RFC 3339
    timestamp = 2022-08-06T11:22:00
    # Location of the game or the server url
    location = "Hamburg"
    # Unsigned Integer
    number_of_teams = 2
    [[players]]
    [[players.player_name_1]]
    # Unsigned Integer: ID of team starting with 0
    team = 0
    [[players.player_name_2]]
    team = 1



.. _TOML: https://toml.io/en/