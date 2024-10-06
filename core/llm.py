import ollama
class llm:

    def __init__(self, model=None, keep_alive=True):
        self.model = model
        self.keep_alive = keep_alive

    def generate(self, prompt):
        respone = ollama.generate(
            model=self.model,
            prompt=prompt,
        )

        if respone:
            return respone["response"]
        
        else:
            print("LLM response not found.")