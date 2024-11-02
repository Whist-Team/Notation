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
    # Unsigned Integer: ID of team starting with 0
    team = 0
    name = "John"
    [[players]]
    team = 1
    Name = "Lucy"

Stack
-----
The data contains one mandatory field ``stack`` that is a list of strings representing a card.
Furthermore it has an optional field ``hands`` that is a table of the players' cards in hand.
One card can be represented with

.. code-block:: toml

    suit = "[♦♣♥♠]"
    rank = "[2-10JQKA]"

.. code-block:: toml


    [[stack.card]]
    suit="heart"
    rank="A"
    [[stack.card]]
    suit="heart"
    rank="K"

    [[hands.player_1]]
    [[hands.player_1.card]]
    suit="heart"
    rank="2"


.. _TOML: https://toml.io/en/