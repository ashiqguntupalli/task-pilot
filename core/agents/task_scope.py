from core.utils import load_prompt
from termcolor import colored

class TaskScopeAgent:
    """
    The TaskScopeAgent is responsible for framing questions to gather information about the high-level scope and complexity of the task.
    It takes a task subject and domain as input and returns a summary of the high-level scope and complexity of the task.

    Attributes:
        memory (MemoryAgent): The memory agent to store variables collected during the workflow.
        llm (LLM): The language model to use for generating questions and summaries.

    Methods:
        run: Runs the TaskScopeAgent to gather information about the high-level scope and complexity of the task.
    """

    def __init__(self, memory=None, llm=None):
        """
        Initializes the TaskScopeAgent with a task subject and domain.
        :param task_subject: The task subject as a string.
        :param task_domain: The task domain as a string.
        """
        self.memory = memory
        self.llm = llm

    def __frame_scope_questions(self):
        """
        Frames questions based on the task subject and domain.
        """

        self.memory.log_message("Framing scope questions started.")

        scope_questions_prompt = load_prompt("task_scope", "scope_questions").format(
            task_subject=self.memory.get_variables("initializer").get("task_subject"),
            task_module=self.memory.get_variables("initializer").get("task_module")
        )

        if scope_questions_prompt:
            scope_questions = self.llm.generate(scope_questions_prompt)
            self.memory.collect_variables("task_scope", {"scope_questions": scope_questions})

            self.memory.log_message("Framing scope questions completed.")

        else:
            print(colored("Scope Questions prompt not found.", "red", attrs=["bold"]))

    def __collect_scope_answers(self, questions):
        """
        Collects answers from the user.
        """
        print(colored(f"Please answer the below question(s) to understand the scope of the task:\n{questions}", "green"))
        answer = input("Your answer for the above question(s): ")

        self.memory.collect_variables("task_scope", {"scope_answer": answer})

    def __summarize_scope(self):
        """
        Summarizes the scope based on the collected answers.
        """

        self.memory.log_message("Summarizing scope started.")

        summary_scope_prompt = load_prompt("task_scope", "summarize_scope").format(
            questions=self.memory.get_variables("task_scope").get("scope_questions"),
            answers=self.memory.get_variables("task_scope").get("scope_answer")
        )

        if summary_scope_prompt:
            summary = self.llm.generate(summary_scope_prompt)
            self.memory.collect_variables("task_scope", {"scope": summary})

            self.memory.log_message("Summarizing scope completed.")

        else:
            print(colored("Summary Scope prompt not found.", "red", attrs=["bold"]))

    def __summarize_scope_collect_user_input(self):
        """
        Summarizes the scope based on the user's input.
        """
        return None

    def run(self):
        """
        Runs the TaskScopeAgent to gather information about the high-level scope and complexity of the task.
        """

        self.memory.log_message("Task Scope agent started from recipe.")

        self.__frame_scope_questions()
        self.__collect_scope_answers(self.memory.get_variables("task_scope").get("scope_questions"))
        self.__summarize_scope()

        self.memory.log_message("Task Scope agent completed.")
