"""GPTClient class to interact with OpenAI API"""

from os import path
from functools import lru_cache
from openai import OpenAI
from json_repair import loads
from jinja2 import Environment, FileSystemLoader, Template
from ankicardmaker.languages import Language
from ankicardmaker.config_parser import ConfigParser


class GPTClient:
    """Class providing a function to interact with OpenAI API"""

    __slots__ = (
        "config_parser",
        "config_file",
        "client",
        "language",
        "prompt_template",
        "openai_model",
        "openai_model_temperature",
    )

    def __init__(self):
        self.config_parser = ConfigParser()
        self.config_file = self.config_parser.get_config_file()
        self.client = self.set_openai_client()
        self.language = Language()
        self.prompt_template = self.get_prompt_template()
        self.openai_model = self.get_openai_model()
        self.openai_model_temperature = self.get_openai_model_temperature()

    @lru_cache(maxsize=1000)
    def get_openai_api_key(self) -> str | None:
        """Get OpenAI API key."""
        return self.config_file["openai"].get("api_key")

    def set_openai_client(self) -> OpenAI:
        """Set OpenAI client."""
        return (
            OpenAI(api_key=self.get_openai_api_key())
            if self.get_openai_api_key()
            else OpenAI()
        )

    @lru_cache(maxsize=1000)
    def get_openai_model(self) -> str:
        """Get OpenAI model."""
        return self.config_file["openai"].get("model", "gpt-4-0125-preview")

    @lru_cache(maxsize=1000)
    def get_openai_model_temperature(self) -> float:
        """Get OpenAI model temperature."""
        return self.config_file["openai"].get("temperature", 0.3)

    @lru_cache(maxsize=1000)
    def get_prompt_template(self) -> Template:
        """Get prompt template."""
        return Environment(
            loader=FileSystemLoader(path.join(path.dirname(__file__), "data")),
            autoescape=True,
        ).get_template("prompt.jinja")

    def create_prompt(self, text: str, language_code: str) -> str:
        """Create prompt."""
        return self.prompt_template.render(
            text=text, language_name=self.language.get_language_name(language_code)
        )

    def check_prompt(self, prompt: str) -> str:
        """Check prompt."""
        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a string")
        return prompt

    def create_gpt_request(self, prompt: str) -> str:
        """Create GPT request."""
        prompt = self.check_prompt(prompt)
        try:
            result = self.client.chat.completions.create(
                model=self.openai_model,
                temperature=self.openai_model_temperature,
                response_format={"type": "json_object"},
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as error:
            raise RuntimeError("Failed to get response from GPT API") from error
        if not result or not result.choices:
            raise ValueError("No response received from GPT API")
        return result.choices[0].message.content

    def get_gpt_response(self, prompt: str) -> dict:
        """Get GPT response."""
        prompt = self.check_prompt(prompt)
        try:
            return loads(self.create_gpt_request(prompt))
        except Exception as error:
            raise ValueError("Failed to parse response from GPT API") from error
