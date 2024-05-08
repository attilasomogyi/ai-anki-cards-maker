# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for parsing command line arguments."""

from argparse import ArgumentParser
from ankicardmaker.modules.command_line.arguments.deck_name import (
    CommandLineArgumentsDeckName,
)
from ankicardmaker.modules.command_line.arguments.file import CommandLineArgumentsFile
from ankicardmaker.modules.command_line.arguments.language import (
    CommandLineArgumentsLanguage,
)
from ankicardmaker.modules.command_line.arguments.version import (
    CommandLineArgumentsVersion,
)
from ankicardmaker.modules.command_line.arguments.verbose import (
    CommandLineArgumentsVerbose,
)


# pylint: disable=too-few-public-methods
class CommandLineParserArgs:
    """Class providing a function to parse command line arguments."""

    @staticmethod
    def parse():
        """Parse command line arguments."""
        parser = ArgumentParser()
        CommandLineArgumentsFile.add(parser)
        CommandLineArgumentsDeckName.add(parser)
        CommandLineArgumentsLanguage.add(parser)
        CommandLineArgumentsVersion.add(parser)
        CommandLineArgumentsVerbose.add(parser)
        return parser.parse_args()
