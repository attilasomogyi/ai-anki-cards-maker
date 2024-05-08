# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling verbose argument."""

from argparse import ArgumentParser


# pylint: disable=too-few-public-methods
class CommandLineArgumentsVerbose:
    """Class providing a function to add verbose argument."""

    @staticmethod
    def add(parser: ArgumentParser):
        """Add verbose argument."""
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            help="Verbose mode",
            action="store_true",
            required=False,
        )
