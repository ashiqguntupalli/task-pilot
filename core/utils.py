import os
import re
from importlib import resources

def load_prompt(agent_name, prompt_name):
    try:
        with resources.path('core.prompts', agent_name) as agent_path:
            prompt_path = os.path.join(agent_path, f'{prompt_name}.prompt')
            
            with open(prompt_path, 'r') as file:
                return file.read().strip()
    except FileNotFoundError:
        print(f"Prompt '{prompt_name}' not found for agent '{agent_name}'.")
        return None

def exclude_tagged_text(text, tag):
    if tag is None:
        return text

    # Regex pattern to match the tag with its content, including any surrounding whitespace
    pattern = re.compile(r'\s*<{}>.*?</{}>\s*'.format(re.escape(tag), re.escape(tag)), re.DOTALL)

    # Replace matched patterns with a single space to maintain proper spacing
    cleaned_text = pattern.sub(' ', text)

    # Optionally, you can also strip leading/trailing spaces and reduce multiple spaces to single
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text