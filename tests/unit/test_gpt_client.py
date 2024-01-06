"""Test GPTClient class."""
# pylint: disable=R0903,W0611

from os import path
from jinja2 import Environment, FileSystemLoader
import pytest  # noqa: F401
from ankicardmaker.gpt_client import GPTClient


class TestGPTClient:
    """Test GPTClient class."""

    def test_create_prompt(self):
        """Test create_prompt function."""
        gpt_client = GPTClient()
        result = gpt_client.create_prompt("test 1", "en")
        template_path = path.join("src", "ankicardmaker", "data")
        environment = Environment(
            loader=FileSystemLoader(template_path), autoescape=True
        )
        template = environment.get_template("prompt.jinja")
        expected = template.render(text="test 1", language_name="English")
        assert result == expected
