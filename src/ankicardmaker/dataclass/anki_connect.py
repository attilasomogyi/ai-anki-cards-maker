# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Dataclass for AnkiConnect."""

from dataclasses import dataclass


@dataclass
class AnkiConnect:
    """Dataclass for AnkiConnect"""

    api_key: str
    url: str
