from core.utils import load_prompt
from termcolor import colored

class StructuringAgent:
    """
    The StructuringAgent is responsible for creating a task structure based on the
    high-level scope and detailed requirements.

    Attributes:
        high_level_scope (dict): The high-level scope of the task.
        detailed_requirements (dict): The detailed requirements of the task.
        task_structure (str): The task structure created by the agent.
    """

    def __init__(self, memory=None, llm=None):
        """
        Initializes the StructuringAgent with the high-level scope and detailed
        requirements.

        Args:
            high_level_scope (dict): The high-level scope of the task.
            detailed_requirements (dict): The detailed requirements of the task.
        """
        self.memory = memory
        self.llm = llm

    def __create_task_structure(self):
        """
        Creates the task structure based on the high-level scope and detailed
        requirements.
        """

        self.memory.log_message("Creating task structure.")

        task_structure_prompt = load_prompt("structuring", "task_structure").format(
            scope=self.memory.get_variables("task_scope").get("scope"),
            detailed_requirements=self.memory.get_variables("requirements").get("detailed_requirements")
        )

        if task_structure_prompt:
            task_structure = self.llm.generate(task_structure_prompt)
            self.memory.collect_variables("structuring", {"task_structure": task_structure})

            self.memory.log_message("Creating task structure completed.")

        else:
            print(colored("Task Structure prompt not found.", "red", attrs=["bold"]))

    def run(self):
        """
        Runs the StructuringAgent to create a task structure based on the
        high-level scope and detailed requirements.
        """

        self.memory.log_message("Structuring agent started from recipe.")

        self.__create_task_structure()

        self.memory.log_message("Structuring agent completed.")
