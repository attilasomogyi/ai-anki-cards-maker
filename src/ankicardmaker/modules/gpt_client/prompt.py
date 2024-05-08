# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to create OpenAI client prompt."""

from ankicardmaker.modules.gpt_client.prompt_template import GPTClientPromptTemplate
from ankicardmaker.modules.language.name import LanguageName


# pylint: disable=too-few-public-methods
class GPTClientPrompt:
    """Class providing a function to create OpenAI client prompt."""

    @staticmethod
    def create(text: str, language_code: str) -> str:
        """Create prompt."""
        return (
            GPTClientPromptTemplate()
            .get()
            .render(text=text, language_name=LanguageName.get(language_code))
        )
