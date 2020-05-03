Othello Documentation
=====================

.. toctree::
   :hidden:
   :maxdepth: 1

   license

A command-line interface for Othello!
Either player can be human or a bot.
A list of available agents is available
via the help command.


Installation
------------

To install the Othello project,
run this command in your terminal:

.. code-block:: console

   $ pip install othello-cli


Usage
-----

.. code-block:: console

   $ othello [OPTIONS]

.. option:: -b <agent>, --black <agent>

   The agent type for black.

.. option:: -w <agent>, --white <agent>

   The agent type for white.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short help message and exit.


Reference
---------

.. toctree::
   :maxdepth: 1

   reference/game
   reference/board
   reference/types
   reference/agents
