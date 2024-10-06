from termcolor import colored

class Initializer:
    """
    Initializes the workflow by collecting user input and interacting with the LLM.
    """

    def __init__(self, memory=None):
        """
        Initializes the Initializer agent with empty task subject and domain.
        """
        self.memory = memory

    def collect_user_input(self):
        """
        Collects user input and parses it into task subject and domain.
        Returns:
            tuple: Task subject and domain as strings.
        """
        print(colored("Hello! I'm here to help you create a task description.", "green"))
        print(colored("To get started, could you please provide a brief description of the task's subject and the module it falls under?", "green"))
        print(colored("Subject and module should be separated by a comma. For example: Subject, Module", "green"))
        user_input = input("Task subject and module: ")

        return self.parse_input(user_input)

    def parse_input(self, user_input):
        """
        Parses the user input into task subject and domain.
        Args:
            user_input (str): User input as a string.
        Returns:
            tuple: Task subject and domain as strings.
        Raises:
            ValueError: If the user input is not a comma-separated string.
        """
        try:
            task_subject, task_module = user_input.split(',')
            return task_subject.strip(), task_module.strip()
        except ValueError:
            print(colored("Invalid input. Please provide a comma-separated string. For example: Subject, Module", "red"))
            return self.collect_user_input()

    def run(self):
        """
        Runs the Initializer agent, collecting user input and interacting with the LLM.
        """

        self.memory.log_message("Initializer agent started from recipe.")

        task_subject, task_module = self.collect_user_input()

        self.memory.collect_variables("initializer", {"task_subject": task_subject, "task_module": task_module})

        self.memory.log_message("Initializer agent completed from recipe.")