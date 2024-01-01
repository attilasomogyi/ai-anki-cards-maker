
import asyncio
import sys
import json
import urllib.request
import pyperclip
import json_repair

from openai import OpenAI

apiKey = "myankikey"


prompt = """You are a professional making flash cards from given text for educational purposes for schools, universities, professional trainnings.
Create as much as needed flash cards following these rules:
- do not do duplicates.
- you only provide the json for the flash cards, do not say anything else in the text, the text will be ignored.
- questions should have all the context necessary for answering it, (not "How was this period called ? " but "How was the period between 1939 and 1945 called ?") because the flash cards will have no other context than the question.
- make global question about the text when it makes sense
- don't invent anything, only use the text
- write in Hungarian
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


{}""".format(''.join(pyperclip.paste()))

print(prompt)

client = OpenAI()

result = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

gpt_response = result.choices[0].message.content
print(gpt_response)
gpt_response = json_repair.loads(gpt_response)

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6, 'key': apiKey}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    print(requestJson)
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
#    if response['error'] is not None:
#        raise Exception(response['error'])
    return response['result']

def make_note(*,deckName="test", front="front1", back="back1", allow_duplicates=False):
    note = {"note": {
        "deckName": deckName,
        "modelName": "Basic",
        "fields": {"Front": front, "Back": back},
        "tags": ["ai-generated"],
    }}

    if allow_duplicates:
        return {**note, "options": {"allowDuplicate": True}}
    else:
        return note

for response in gpt_response['flashcards']:
    invoke('addNote', **make_note(deckName='test',front=response['question'], back=response['answer']))
