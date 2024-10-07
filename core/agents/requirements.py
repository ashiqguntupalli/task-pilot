from core.utils import load_prompt
from termcolor import colored

class RequirementsAgent:
    """
    The RequirementsAgent class is responsible for asking the user questions to gather more detailed requirements.
    It takes a high-level scope as input and returns a dictionary with the detailed requirements.
    """

    def __init__(self, memory=None, llm=None):
        """
        Initialize the RequirementsAgent with a high-level scope.
        :param memory: The memory agent to store variables collected during the workflow.
        :param llm: The language model to use for generating questions and summaries.
        """
        self.memory = memory
        self.llm = llm

    def __frame_requirement_questions(self):
        """
        Frame questions to gather requirements.
        """

        self.memory.log_message("Framing requirement questions started.")

        requirement_questions_prompt = load_prompt("requirements", "requirement_questions").format(
            scope=self.memory.get_variables("task_scope").get("scope")
        )

        if requirement_questions_prompt:
            requirement_questions = self.llm.generate(requirement_questions_prompt)
            self.memory.collect_variables("requirements", {"requirement_questions": requirement_questions})

            self.memory.log_message("Framing requirement questions completed.")

        else:
            print(colored("Requirement Questions prompt not found.", "red", attrs=["bold"]))

    def __collect_requirement_answers(self, requirement_questions):
        """
        Collect answers from the user.
        """
        print("\n")
        print(colored(f"Please answer the above question(s) to understand the further requirements of the task:\n{requirement_questions}", "green"))
        print("\n")

        answer = input("Your answer for the above question(s): ")

        self.memory.collect_variables("requirements", {"requirement_answers": answer})

    def __create_detailed_requirements_list(self):
        """
        Create a list of detailed requirements.
        """

        self.memory.log_message("Creating detailed requirements list.")
        
        detailed_requirements_prompt = load_prompt("requirements", "detailed_requirements").format(
            scope=self.memory.get_variables("task_scope").get("scope"),
            requirement_questions=self.memory.get_variables("requirements").get("requirement_questions"),
            requirement_answers=self.memory.get_variables("requirements").get("requirement_answers")
        )

        if detailed_requirements_prompt:
            detailed_requirements = self.llm.generate(detailed_requirements_prompt)
            self.memory.collect_variables("requirements", {"detailed_requirements": detailed_requirements})

            self.memory.log_message("Creating detailed requirements list completed.")

        else:
            print(colored("Detailed Requirements prompt not found.", "red", attrs=["bold"]))

    def run(self):
        """
        Run the RequirementsAgent to gather detailed requirements.
        """

        self.memory.log_message("Requirements agents started from recipe.")

        self.__frame_requirement_questions()
        self.__collect_requirement_answers(self.memory.get_variables("requirements").get("requirement_questions"))
        self.__create_detailed_requirements_list()

        self.memory.log_message("Requirements agents completed.")