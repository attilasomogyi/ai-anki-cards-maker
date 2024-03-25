# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for GPTClient."""

from ankicardmaker.gpt_client import GPTClient
from ankicardmaker.config_parser import ConfigParser

# pylint: disable=protected-access


class TestGPTClient:
    """Test class for GPTClient."""

    def test_init(self):
        """Test __init__."""
        gpt_client = GPTClient()
        assert gpt_client._GPTClient__config_file == ConfigParser().get_config_file()

    def test_get_base_url_is_none(self):
        """Test __get_base_url."""
        gpt_client = GPTClient()
        assert gpt_client._GPTClient__get_base_url() is None
