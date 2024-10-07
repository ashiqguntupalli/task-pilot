import logging
from core.agents.orchestrator import OrchestratorAgent
from core.agents.memory import MemoryAgent
from core.llm import llm
import argparse

class llm_test:
    def __init__(self):
        pass

    def generate(self, prompt):
        return "dummy answer"

def configure_logging(enabled=False):
    if enabled:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.disable(logging.CRITICAL)

def main():
    parser = argparse.ArgumentParser(description="Task pilot")
    parser.add_argument('-m', '--model', type=str, default="llama3.2:3b", help="LLM model to use")
    parser.add_argument('-l', '--log', action="store_true", help="Enable logging")

    args = parser.parse_args()

    configure_logging(args.log)

    llm_instance = llm(model=args.model)

    memory = MemoryAgent(disable_logging=not args.log)

    orchestrator = OrchestratorAgent(memory=memory, llm=llm_instance)
    orchestrator.run()

if __name__ == "__main__":
    main()