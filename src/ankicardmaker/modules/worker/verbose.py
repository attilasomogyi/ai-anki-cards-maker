# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling verbose mode."""

from pprint import pprint


# pylint: disable=too-few-public-methods
class WorkerVerbose:
    """Class providing a function to handle verbose mode."""

    @staticmethod
    def print(section):
        """Print section in verbose mode."""
        print("GPT response:")
        pprint(section)
        print()
