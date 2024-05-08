# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling OpenAI client."""

from functools import cache
from openai import OpenAI
from ankicardmaker.modules.gpt_client.api_key import GPTClientAPIKey
from ankicardmaker.modules.gpt_client.base_url import GPTClientBaseURL


# pylint: disable=too-few-public-methods
class GPTClient:
    """Class providing a function to get OpenAI client."""

    @staticmethod
    @cache
    def set() -> OpenAI:
        """Set OpenAI client."""
        api_key = GPTClientAPIKey().get()
        base_url = GPTClientBaseURL().get()
        return (
            OpenAI(api_key=api_key, base_url=base_url)
            if api_key
            else OpenAI(base_url=base_url)
        )
