# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling language argument."""

from argparse import ArgumentParser
from ankicardmaker.modules.language.codes import LanguageCodes


# pylint: disable=too-few-public-methods
class CommandLineArgumentsLanguage:
    """Class providing a function to add language argument."""

    @staticmethod
    def add(parser: ArgumentParser):
        """Add language argument."""
        parser.add_argument(
            "-l",
            "--language",
            dest="language_code",
            help="Language code",
            choices=LanguageCodes.get(),
            default="en",
            nargs=1,
            type=str,
        )
