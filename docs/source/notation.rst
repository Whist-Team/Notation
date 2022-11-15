Card Game Notation Standard
===========================
This standard uses TOML_ as notation language.

Header
-------
All meta data is defined in the Header. This contains information about teams and players.

.. code-block:: toml
    :caption: Header Example
    [header]
    # Unsigned Integer
    number_of_teams = 2
    # List of dictionaries
    players = [{ name="Player 1", team=0 }, { player="Player 2", team=1 }




.. _TOML: https://toml.io/en/