"""GPTClient class to interact with OpenAI API"""

from os import path
from openai import OpenAI
from json_repair import loads
from jinja2 import Environment, FileSystemLoader
from ankicardmaker.languages import Language


class GPTClient:
    """Class providing a function to interact with OpenAI API"""

    def __init__(self):
        self.client = OpenAI()
        self.language = Language()
        template_path = path.join(path.dirname(__file__), "data")
        environment = Environment(
            loader=FileSystemLoader(template_path), autoescape=True
        )
        self.template = environment.get_template("prompt.jinja")

    def create_prompt(self, text, language_code):
        """Create a prompt."""
        language_name = self.language.get_language_name(language_code)
        prompt = self.template.render(text=text, language_name=language_name)
        return prompt

    def get_gpt_response(self, prompt):
        """Get GPT response."""
        if not prompt:
            raise ValueError("Prompt is required")

        result = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=0.1,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
        )

        gpt_response = str(result.choices[0].message.content)
        gpt_response = loads(gpt_response)
        return gpt_response
