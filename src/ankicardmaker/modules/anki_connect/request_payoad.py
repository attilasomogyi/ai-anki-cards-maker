# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to create Anki request payloads."""


# pylint: disable=too-few-public-methods
class AnkiConnectRequestPayload:
    """Class providing a function to create Anki request payloads."""

    def __init__(self, anki_connect_api_key: str):
        self.__anki_connect_api_key = anki_connect_api_key

    def create(
        self,
        action: str,
        **parameters: dict,
    ) -> dict:
        """Create a request payload."""
        return {
            "action": action,
            "params": parameters,
            "version": 6,
            "key": self.__anki_connect_api_key,
        }
