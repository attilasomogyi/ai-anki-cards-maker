# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling deck name argument."""

from argparse import ArgumentParser


# pylint: disable=too-few-public-methods
class CommandLineArgumentsDeckName:
    """Class providing a function to add deck name argument."""

    @staticmethod
    def add(parser: ArgumentParser):
        """Add deck name argument."""
        parser.add_argument(
            "-d",
            "--deck",
            dest="deck_name",
            help="Deck name",
            required=True,
            nargs=1,
            type=str,
        )
