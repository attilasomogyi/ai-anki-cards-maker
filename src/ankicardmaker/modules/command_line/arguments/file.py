# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling file argument."""

from argparse import ArgumentParser


# pylint: disable=too-few-public-methods
class CommandLineArgumentsFile:
    """Class providing a function to add file argument."""

    @staticmethod
    def add(parser: ArgumentParser):
        """Add file argument."""
        parser.add_argument(
            "-f",
            "--file",
            dest="file_path",
            help="File path",
            required=False,
            nargs=1,
            type=str,
        )
