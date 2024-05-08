# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to create GPT request."""

from json_repair import loads
from ankicardmaker.modules.gpt_client.gpt_client import GPTClient
from ankicardmaker.modules.gpt_client.model import GPTClientModel
from ankicardmaker.modules.gpt_client.model_temperature import GPTClientModelTemperature


# pylint: disable=too-few-public-methods
class GPTClientRequest:
    """Class providing a function to create GPT request."""

    @staticmethod
    def execute(prompt: str) -> dict:
        """Create GPT request."""
        if not prompt:
            raise ValueError("Prompt must be a non-empty string.")
        try:
            openai = GPTClient.set()
            # pylint: disable=no-member
            result = openai.chat.completions.create(
                model=GPTClientModel.get(),
                temperature=GPTClientModelTemperature.get(),
                response_format={"type": "json_object"},
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as error:
            raise RuntimeError("Failed to get response from GPT API.") from error
        if not result or not result.choices:
            raise ValueError("No response received from GPT API.")
        return loads(result.choices[0].message.content)
