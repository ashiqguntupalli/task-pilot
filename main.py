import logging
from core.agents.orchestrator import OrchestratorAgent
from core.agents.memory import MemoryAgent
from core.llm import llm

class llm_dummy:
    def __init__(self):
        pass

    def generate(self, prompt):
        return "dummy answer"

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the task pilot workflow...")

    llm_instance = llm(model="llama3.2:3b")

    memory = MemoryAgent()

    orchestrator = OrchestratorAgent(memory=memory, llm=llm_instance)
    orchestrator.run()

if __name__ == "__main__":
    main()