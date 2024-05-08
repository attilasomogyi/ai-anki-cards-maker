# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling version argument."""

from argparse import ArgumentParser


# pylint: disable=too-few-public-methods
class CommandLineArgumentsVersion:
    """Class providing a function to add version argument."""

    @staticmethod
    def add(parser: ArgumentParser):
        """Add version argument."""
        parser.add_argument("--version", action="version", version="%(prog)s 0.1")
