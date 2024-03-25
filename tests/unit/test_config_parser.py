# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for the ConfigParser class."""

from unittest.mock import patch, mock_open
from pathlib import Path
from jsonschema.exceptions import ValidationError
import pytest
from ankicardmaker.config_parser import ConfigParser

# pylint: disable=protected-access
# pylint: disable=assigning-non-slot
# flake8: noqa: W503


class TestConfigParser:
    """Test class for ConfigParser."""

    def test_init(self):
        """Test __init__."""
        config_parser = ConfigParser()
        assert config_parser._ConfigParser__home_dir == Path.home()
        assert config_parser._ConfigParser__config_file_name == "ankicardmaker.toml"
        assert config_parser._ConfigParser__json_schema_path in [
            Path(__file__).parents[2]
            / "src"
            / "ankicardmaker"
            / "data"
            / "ankicardmaker_config_file_schema.json",
            None,
        ]
        assert config_parser._ConfigParser__json_schema is not None

    def test_get_json_schema(self):
        """Test __get_json_schema."""
        config_parser = ConfigParser()
        assert config_parser._ConfigParser__get_json_schema() is not None
        config_parser._ConfigParser__json_schema_path = Path("test")
        with pytest.raises(ValueError):
            config_parser._ConfigParser__get_json_schema()

    def test_get_config_file_path(self):
        """Test __get_config_file_path."""
        config_parser = ConfigParser()
        with patch("ankicardmaker.config_parser.system", return_value="Linux"):
            assert (
                config_parser._ConfigParser__get_config_file_path()
                == Path.home() / ".config" / "ankicardmaker.toml"
            )
        with patch("ankicardmaker.config_parser.system", return_value="Darwin"):
            assert (
                config_parser._ConfigParser__get_config_file_path()
                == Path.home()
                / "Library"
                / "Application Support"
                / "ankicardmaker.toml"
            )
        with patch("ankicardmaker.config_parser.system", return_value="Windows"):
            assert (
                config_parser._ConfigParser__get_config_file_path()
                == Path.home() / "AppData" / "Roaming" / "ankicardmaker.toml"
            )
        with patch("ankicardmaker.config_parser.system", return_value="Unsupported"):
            with pytest.raises(ValueError):
                config_parser._ConfigParser__get_config_file_path()

    def test_get_config_file(self):
        """Test get_config_file."""
        parser = ConfigParser()
        with patch("builtins.open", mock_open()) as mocked_open:
            mocked_open.side_effect = FileNotFoundError()
            assert parser.get_config_file() is None
        with patch("builtins.open", mock_open()) as mocked_open:
            mocked_open.side_effect = IOError()
            with pytest.raises(ValueError):
                parser.get_config_file()

    def test_validate_config_file(self):
        """Test __validate_config_file."""
        config_parser = ConfigParser()
        config_file = {
            "openai": {
                "api_key": "test_api_key",
                "model": "test_model",
                "temperature": 0.3,
            }
        }
        assert (
            config_parser._ConfigParser__validate_config_file(config_file)
            == config_file
        )
        not_valid_config_file = {"test": "test"}
        with pytest.raises(ValidationError):
            config_parser._ConfigParser__validate_config_file(not_valid_config_file)
        config_parser._ConfigParser__json_schema = None
        with pytest.raises(ValueError):
            config_parser._ConfigParser__validate_config_file(config_file)
