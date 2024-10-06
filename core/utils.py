import os
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