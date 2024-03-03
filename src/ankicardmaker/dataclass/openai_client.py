# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Dataclass for OpenAIClient."""

from dataclasses import dataclass


@dataclass
class OpenAIClient:
    """Dataclass for OpenAIClient."""

    client: object
    model: str
    model_temperature: float
