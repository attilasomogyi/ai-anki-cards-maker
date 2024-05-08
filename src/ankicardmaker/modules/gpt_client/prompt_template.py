# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to get OpenAI prompt template."""

from os import path
from functools import cache
from jinja2 import Environment, FileSystemLoader, Template


# pylint: disable=too-few-public-methods
class GPTClientPromptTemplate:
    """Class providing a function to get OpenAI prompt template."""

    @staticmethod
    @cache
    def get() -> Template:
        """Get prompt template."""
        return Environment(
            loader=FileSystemLoader(path.join(path.dirname(__file__), "template")),
            autoescape=True,
        ).get_template("prompt.jinja")
