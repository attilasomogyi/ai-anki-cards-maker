# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""GPTClient class to interact with OpenAI API"""

from os import path
from functools import lru_cache
from openai import OpenAI
from openai import base_url
from json_repair import loads
from jinja2 import Environment, FileSystemLoader, Template
from ankicardmaker.dataclass.openai_client import OpenAIClient
from ankicardmaker.languages import Language
from ankicardmaker.config_parser import ConfigParser


class GPTClient:
    """Class providing a function to interact with OpenAI API"""

    __slots__ = (
        "__config_file",
        "__language",
        "__prompt_template",
        "__openai",
    )

    def __init__(self):
        self.__config_file = ConfigParser().get_config_file()
        self.__openai = OpenAIClient(
            client=self.__set_openai_client(),
            model=self.__get_openai_model(),
            model_temperature=self.__get_openai_model_temperature(),
        )
        self.__language = Language()
        self.__prompt_template = self.__get_prompt_template()

    @lru_cache(maxsize=1)
    def __get_base_url(self) -> str:
        """Get base URL."""
        return self.__config_file["openai"].get("base_url", base_url)

    @lru_cache(maxsize=1)
    def __get_openai_api_key(self) -> str | None:
        """Get OpenAI API key."""
        return self.__config_file["openai"].get("api_key")

    def __set_openai_client(self) -> OpenAI:
        """Set OpenAI client."""
        return (
            OpenAI(api_key=self.__get_openai_api_key(), base_url=self.__get_base_url())
            if self.__get_openai_api_key()
            else OpenAI(base_url=self.__get_base_url())
        )

    @lru_cache(maxsize=1)
    def __get_openai_model(self) -> str:
        """Get OpenAI model."""
        return self.__config_file["openai"].get("model", "gpt-4-0125-preview")

    @lru_cache(maxsize=1)
    def __get_openai_model_temperature(self) -> float:
        """Get OpenAI model temperature."""
        return self.__config_file["openai"].get("temperature", 0.3)

    @lru_cache(maxsize=1)
    def __get_prompt_template(self) -> Template:
        """Get prompt template."""
        return Environment(
            loader=FileSystemLoader(path.join(path.dirname(__file__), "data")),
            autoescape=True,
        ).get_template("prompt.jinja")

    def create_prompt(self, text: str, language_code: str) -> str:
        """Create prompt."""
        return self.__prompt_template.render(
            text=text, language_name=self.__language.get_language_name(language_code)
        )

    def __check_prompt(self, prompt: str) -> str:
        """Check prompt."""
        if not prompt:
            raise ValueError("Prompt must be a non-empty string.")
        return prompt

    def __create_gpt_request(self, prompt: str) -> str:
        """Create GPT request."""
        prompt = self.__check_prompt(prompt)
        try:
            # pylint: disable=no-member
            result = self.__openai.client.chat.completions.create(
                model=self.__openai.model,
                temperature=self.__openai.model_temperature,
                response_format={"type": "json_object"},
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as error:
            raise RuntimeError("Failed to get response from GPT API.") from error
        if not result or not result.choices:
            raise ValueError("No response received from GPT API.")
        return result.choices[0].message.content

    def get_gpt_response(self, prompt: str) -> dict:
        """Get GPT response."""
        prompt = self.__check_prompt(prompt)
        try:
            return loads(self.__create_gpt_request(prompt))
        except Exception as error:
            raise ValueError("Failed to parse response from GPT API.") from error
