# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Worker module for the Anki Card Maker application."""

from ankicardmaker.modules.worker.notes import WorkerNotes
from ankicardmaker.modules.worker.notes_to_anki import WorkerNotesToAnki
from ankicardmaker.modules.worker.arguments import WorkerArguments
from ankicardmaker.modules.gpt_client.prompt import GPTClientPrompt
from ankicardmaker.modules.gpt_client.request import GPTClientRequest
from ankicardmaker.modules.worker.verbose import WorkerVerbose


# pylint: disable=too-few-public-methods
class WorkerRun:
    """Worker class for the Anki Card Maker application."""

    @staticmethod
    def run(clipboard: str, deck_name: str, language_code: str, verbose: bool = False):
        """Worker function."""
        WorkerArguments.test(clipboard, deck_name, language_code)
        prompt = GPTClientPrompt.create(clipboard, language_code)
        gpt_response = GPTClientRequest.execute(prompt)
        if verbose:
            WorkerVerbose.print(gpt_response)
        try:
            notes = WorkerNotes.create(deck_name, gpt_response)
        except ValueError as error:
            raise ValueError(f"Failed to create notes: {error}") from error
        WorkerNotesToAnki.add(notes)
