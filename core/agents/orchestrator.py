from core.agents.initializer import Initializer
from core.agents.task_scope import TaskScopeAgent
from core.agents.requirements import RequirementsAgent
from core.agents.structuring import StructuringAgent
from core.agents.refinement import RefinementAgent

class OrchestratorAgent:
    """
    Orchestrates the workflow by running the agents in sequence and passing the output from one agent as input to the next agent.
    """

    def __init__(self, memory=None, llm=None):
        """
        Initializes the OrchestratorAgent with a list of agents to run in sequence.
        """

        self.memory = memory

        self.agents = [
            {"name": "initializer", "instance": Initializer(self.memory)},
            {"name": "task_scope", "instance": TaskScopeAgent(self.memory, llm)},
            {"name": "requirements", "instance": RequirementsAgent(self.memory, llm)},
            {"name": "structuring", "instance": StructuringAgent(self.memory, llm)},
            {"name": "refinement", "instance": RefinementAgent(self.memory, llm)}
        ]

    def run(self, llm=None):
        """
        Runs the workflow by running the agents in sequence and passing the output from one agent as input to the next agent.
        """

        self.memory.log_message("Orchestrator started agentic recipe.")

        for agent in self.agents:
            agent["instance"].run()

        self.memory.log_message("Orchestrator completed recipe.")