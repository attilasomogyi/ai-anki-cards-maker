<!--
SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
SPDX-License-Identifier: AGPL-3.0-or-later
-->

# GPT Client

[Visit the table of contents](README.md)

The active selection is a Python class named `GPTClient` that is used to
interact with the OpenAI GPT-3 model. This class is part of a larger
project that appears to be a tool for creating Anki flashcards using the
GPT-3 model.

The `GPTClient` class uses the `OpenAI` class from the `openai` module
to interact with the GPT-3 model. The `OpenAI` class is a client for the
OpenAI API, which provides methods for creating completions, chat
messages, edits, embeddings, files, images, audio, moderations, models,
fine-tuning, fine-tunes, and beta. The `OpenAI` class also provides
methods for setting and getting client options such as the API key,
organization, base URL, timeout, max retries, default headers, default
query, HTTP client, and strict response validation.

In the `__init__` method of the `GPTClient` class, an `OpenAI` object
and a `Language` object are created. The `Language` class is imported
from the `ankicardmaker.languages` module. This class appears to load a
list of languages from a JSON file and provides methods to get language
codes and names.

The `create_prompt` method of the `GPTClient` class creates a prompt for
the GPT-3 model. The prompt is a string that instructs the model to
create flashcards from a given text in a specified language. The rules
for creating the flashcards are included in the prompt. The `format`
method is used to insert the text into the prompt.

The `get_gpt_response` method of the `GPTClient` class sends the prompt
to the GPT-3 model and gets the response. The `chat.completions.create`
method of the `OpenAI` object is used to send the prompt. The response
from the model is a JSON object, which is parsed using the `loads`
function from the `json_repair` module. If the prompt is empty, a
`ValueError` is raised.
