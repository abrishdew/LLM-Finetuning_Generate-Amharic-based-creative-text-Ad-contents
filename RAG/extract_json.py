import json
import re

def extract_json(json_file):
    last_25_percent_text = ""

    # Load data from the provided JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
        messages = data.get('messages', [])

        last_25_percent_length = int(len(messages) * 0.25)
        for message in messages[-last_25_percent_length:]:
            # Extract 'text' content only from the top-level key
            parent_text = message.get('text', None)
            if isinstance(parent_text, str):
                last_25_percent_text += parent_text

    # Remove specific characters using re.sub
    cleaned_text = re.sub(r'[!@#$%^&*()_+~=-{}|"?><`.]', '', last_25_percent_text)

    return cleaned_text
