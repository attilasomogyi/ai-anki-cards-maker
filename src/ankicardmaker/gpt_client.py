"""GPTClient class to interact with OpenAI API"""

from openai import OpenAI
from json_repair import loads
from ankicardmaker.languages import Language


class GPTClient:
    """Class providing a function to interact with OpenAI API"""

    def __init__(self):
        self.client = OpenAI()
        self.language = Language()

    def create_prompt(self, text, language_code):
        """Create a prompt."""
        language_name = self.language.get_language_name(language_code)
        prompt = f"""You are a professional making flash cards from given text for educational purposes for schools, universities, professional trainnings.
        Create as much as needed flash cards following these rules:
        - do not do duplicates.
        - you only provide the json for the flash cards, do not say anything else in the text, the text will be ignored.
        - questions should have all the context necessary for answering it, (not "How was this period called ? " but "How was the period between 1939 and 1945 called ?") because the flash cards will have no other context than the question.
        - make global question about the text when it makes sense
        - don't invent anything, only use the text
        - write in {language_name}
        - format:
        {{
            flashcards: [
            {{
               "question": "question",
               "answer": "answer"
            }},
            {{
               "question": "question",
               "answer": "answer"
            }}
            ]
        }}
        
        \n{text}""".format(
            text, language_name
        )
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

        gpt_response = result.choices[0].message.content
        gpt_response = loads(gpt_response)
        return gpt_response
