<!--
SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
SPDX-License-Identifier: AGPL-3.0-or-later
-->

# Anki card maker

[Visit the table of contents](README.md)

The active selection is a Python class named `AnkiCardMaker`. This class
is designed to interact with the Anki flashcard software's API.

In the `__init__` method of the `AnkiCardMaker` class, it tries to get
the value of the `ANKI_API_KEY` environment variable using the `getenv`
function from the `os` module. If the environment variable is not set,
it raises an exception and exits the program. It also sets the `url`
attribute to the local address where the Anki API server is running.

The `request` method is a helper function that constructs a dictionary
with the necessary fields for making a request to the Anki API. It takes
an action and any number of parameters, and returns a dictionary
containing the action, parameters, version, and API key.

The `invoke` method sends a request to the Anki API and returns the
result. It first serializes the request dictionary to a JSON string
using the `dumps` function from the `json` module, and encodes it to
bytes. It then sends a POST request to the Anki API server with the JSON
string as the body, using the `urlopen` function and the `Request` class
from the `urllib.request` module. The response from the server is
deserialized back into a Python object using the `load` function from
the `json` module. The method then checks the response for errors and
returns the result.

The `make_note` method creates a note dictionary with the given deck
name, front text, back text, and an optional flag to allow duplicates.
If any of the required parameters are missing, it raises a `ValueError`.
The note dictionary is structured according to the Anki API's
requirements for creating a note. If the `allow_duplicates` flag is set
to `True`, it adds an "allowDuplicate" option to the note.

This class can be used to automate the process of creating Anki
flashcards from a Python script. For example, you might use it in a
script that extracts information from a text or a webpage and creates
flashcards from it.
