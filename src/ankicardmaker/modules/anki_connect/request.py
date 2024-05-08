# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to execute Anki request payloads."""

from json import dumps, load
import contextlib
from urllib.request import urlopen, Request
from warnings import warn
from ankicardmaker.modules.anki_connect.request_payoad import AnkiConnectRequestPayload
from ankicardmaker.modules.anki_connect.api_key import AnkiConnectApiKey
from ankicardmaker.modules.anki_connect.url import AnkiConnectUrl


# pylint: disable=too-few-public-methods
class AnkiConnectRequest:
    """Class providing a function to execute Anki request payloads."""

    @staticmethod
    def execute(action: str, **parameters: dict):
        """Invoke an action."""
        anki_connect_api_key = AnkiConnectApiKey().get()
        anki_connect_url = AnkiConnectUrl().get()
        request = Request(
            anki_connect_url,
            dumps(
                AnkiConnectRequestPayload(anki_connect_api_key).create(
                    action, **parameters
                )
            ).encode("utf-8"),
        )
        with contextlib.closing(urlopen(request)) as response:
            response = load(response)
            if response["error"] is not None:
                if (
                    response["error"]
                    not in "Cannot create note because it is a duplicate"
                ):
                    warn(response["error"].capitalize(), RuntimeWarning)
                else:
                    raise ValueError(response["error"].capitalize())
            return response["result"]
