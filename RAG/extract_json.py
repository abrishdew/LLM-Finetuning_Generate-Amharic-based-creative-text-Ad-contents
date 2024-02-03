import json
import re

def extract_json(json_file):
    last_25_percent_text = ""

    # Load data from the provided JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
        messages = data.get('messages', [])

        last_25_percent_length = int(len(messages) * 0.99)
        for message in messages[-last_25_percent_length:]:
            # Extract 'text' content from the top level 'text' key
            text_content = message.get('text', [])

            # Handle the case where 'text' is a list of strings and dictionaries
            if isinstance(text_content, list):
                for item in text_content:
                    if isinstance(item, str):
                        last_25_percent_text += item

    # Remove specific characters using re.sub
    cleaned_text = re.sub(r'[!@#$%^&*()_+~=-{}|"?><`.]', '', last_25_percent_text)

    return last_25_percent_text
