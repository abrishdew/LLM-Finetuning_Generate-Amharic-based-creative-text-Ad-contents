import json
import re


class Util():
    def __init__(self) -> None:
        self.emoji_pattern = re.compile("["
                                        u"\U0001F600-\U0001F64F"  # Emoticons
                                        u"\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
                                        u"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
                                        u"\U0001F700-\U0001F77F"  # Alchemical Symbols
                                        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                                        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                                        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                                        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                                        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                                        u"\u2600-\u26FF"  # Miscellaneous Symbols
                                        u"\u2700-\u27BF"  # Dingbats
                                        u"\u2B50"  # Star
                                        u"\U0001F1E6-\U0001F1FF"  # Country Flags
                                        "]+", flags=re.UNICODE)
        self.symbols = re.compile("["
                                  "\""
                                  "\“"
                                  "\""
                                  "\'"
                                  "\-"
                                  "\*"
                                  "\•"
                                  "\ℹ"
                                  "\﻿"
                                  "\_"
                                  "]+")
        self.url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        self.mention_pattern = r'@(\w+)'

    def read_file(self, file_path: str) -> dict:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Load the JSON data from the file
            data = json.load(file)
            return data

    def write_file(self, file_path: str, data: dict) -> None:
        # Open the file for writing
        with open(file_path, 'w') as file:
            # Dump the JSON data to the file
            json.dump(data, file, indent=2)

    def parse_text(self, text: any) -> str:
        if isinstance(text, str):
            return text
        elif isinstance(text, list):
            contents = []
            for item in text:
                if isinstance(item, str):
                    contents.append(item)
                elif isinstance(item, dict):
                    contents.append(item['text'])
            return "".join(contents)
        else:
            return ""

    def parse_messages(self, messages: list) -> dict:
        parsed_messages = {
            'id': [],
            'text': [],
            'date': []
        }
        for message in messages:
            if message['type'] != 'message' or len(message['text']) == 0:
                continue
            parsed_messages['id'].append(message['id'])
            message_content = self.parse_text(message['text'])
            parsed_messages['text'].append(message_content)
            parsed_messages['date'].append(message['date'])
        return parsed_messages

    def extract_hashtags(self, text: str) -> list:
        return [word for word in text.split() if word.startswith('#')]

    def extract_emojis(self, text):
        return ''.join(self.emoji_pattern.findall(text))

    def remove_emojis(self, text):
        return self.emoji_pattern.sub('', text)

    def extract_symbols(self, text):
        return ''.join(self.symbols.findall(text))

    def remove_symbols(self, text):
        return self.symbols.sub(' ', text)

    def extract_urls(self, text):
        return re.findall(self.url_pattern, text)

    def extract_mentions(self, text):
        return re.findall(self.mention_pattern, text)
