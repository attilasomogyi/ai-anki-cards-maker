# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling notes to Anki."""

from ankicardmaker.modules.anki_connect.request import AnkiConnectRequest


# pylint: disable=too-few-public-methods
class WorkerNotesToAnki:
    """Class providing a function to add notes to Anki."""

    @staticmethod
    def add(notes: list) -> None:
        """Create notes in Anki."""
        if not notes:
            raise ValueError("No notes to add.")
        for note in notes:
            try:
                AnkiConnectRequest.execute("addNote", **note)
            except ValueError as error:
                raise ValueError(f"Failed to add note: {error}") from error
