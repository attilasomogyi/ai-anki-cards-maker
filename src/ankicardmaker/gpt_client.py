"""GPTClient class to interact with OpenAI API"""

from os import path
from openai import OpenAI
from json_repair import loads
from jinja2 import Environment, FileSystemLoader
from ankicardmaker.languages import Language
from ankicardmaker.config_parser import ConfigParser


class GPTClient:
    """Class providing a function to interact with OpenAI API"""

    def __init__(self):
        self.config_parser = ConfigParser()
        self.config_file = self.config_parser.get_config_file()
        self.client = self.set_openai_client()
        self.language = Language()
        self.prompt_template = self.get_prompt_template()

    def get_openai_api_key(self):
        """Get API key."""
        openai_api_key = self.config_file["openai"]["api_key"]
        if not openai_api_key:
            return None
        return openai_api_key

    def set_openai_client(self):
        """Set OpenAI."""
        openai_api_key = self.get_openai_api_key()
        if openai_api_key:
            return OpenAI(api_key=openai_api_key)
        return OpenAI()

    def get_openai_model(self):
        """Get OpenAI model."""
        openai_model = self.config_file["openai"]["model"]
        if openai_model:
            return openai_model
        return "gpt-4-0125-preview"

    def get_openai_model_temperature(self):
        """Get model temperature."""
        openai_temperature = self.config_file["openai"]["temperature"]
        if openai_temperature:
            return openai_temperature
        return 0.3

    def get_prompt_template(self):
        """Get prompt template."""
        template_path = path.join(path.dirname(__file__), "data")
        environment = Environment(
            loader=FileSystemLoader(template_path), autoescape=True
        )
        return environment.get_template("prompt.jinja")

    def create_prompt(self, text, language_code):
        """Create a prompt."""
        language_name = self.language.get_language_name(language_code)
        prompt = self.prompt_template.render(text=text, language_name=language_name)
        return prompt

    def check_prompt(self, prompt):
        """Check prompt."""
        if not prompt:
            raise ValueError("Prompt is required")
        if not isinstance(prompt, str):
            raise TypeError("Prompt must be a string")
        return prompt

    def create_gpt_request(self, prompt):
        """Create GPT request."""
        prompt = self.check_prompt(prompt)
        try:
            result = self.client.chat.completions.create(
                model=self.get_openai_model(),
                temperature=self.get_openai_model_temperature(),
                response_format={"type": "json_object"},
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as error:
            raise RuntimeError("Failed to get response from GPT API") from error
        if not result or not result.choices:
            raise ValueError("No response received from GPT API")
        return str(result.choices[0].message.content)

    def get_gpt_response(self, prompt):
        """Get GPT response."""
        prompt = self.check_prompt(prompt)
        gpt_response = self.create_gpt_request(self.check_prompt(prompt))
        try:
            gpt_response = loads(gpt_response)
        except Exception as error:
            raise ValueError("Failed to parse response from GPT API") from error
        return gpt_response
