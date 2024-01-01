from json import load

class Language:
    def __init__(self):
        with open('language_codes.json') as language_codes_json_file:
            self.languages = load(language_codes_json_file)

    def get_language_codes(self):
        language_list = []
        for language in self.languages:
            language_list.append(language['code'])
        return language_list
    
    def get_language_name(self, language_code):
        for language in self.languages:
            if language['code'] == language_code:
                return language['name']
        return None
