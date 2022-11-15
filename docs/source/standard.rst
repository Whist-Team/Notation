Card Game Notation Standard
===========================
This standard uses TOML_ as notation language.

Header
-------
All meta data is defined in the Header. This contains information about teams and players.

.. code-block::
    [header]
    # Unsigned Integer
    number_of_teams = 2

    [[players]]
    [[player.player_name_1]]
    # Unsigned Integer: ID of team starting with 0
    team = 0
    [[player.player_name_2]]
    team = 1



.. _TOML: https://toml.io/en/