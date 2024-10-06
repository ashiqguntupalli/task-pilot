from termcolor import colored

class RefinementAgent:
    """
    The RefinementAgent is responsible for refining the task description
    based on user input. It will show the current task description, ask if
    further input is needed, and refine the task description based on user
    input.
    """

    def __init__(self, memory=None, llm=None):
        """
        Initializes the RefinementAgent with the task description.
        :param task_structure: The task description as a string.
        """
        self.memory = memory
        self.llm = llm

    def __show_task_description(self):
        """
        Shows the current task description.
        """
        print(colored("\nCurrent Task Description:", "green"))
        print(colored(self.memory.get_variables("structuring").get("task_structure"), "green"))
    def __ask_if_further_input_needed(self):
        """
        Asks if further input is needed.
        :return: The user's input as a string.
        """
        return None

    def __refine_task_description(self, user_input):
        """
        Refines the task description based on user input.
        :param user_input: The user's input as a string.
        """
        return None

    def run(self):
        """
        Runs the RefinementAgent to refine the task description based on user input.
        """

        self.memory.log_message("Refinement agent started from recipe.")

        self.__show_task_description()

        self.memory.log_message("Refinement agent completed.")

        """ while True:
            # Show the current task description
            self.__show_task_description()
            # Ask if further input is needed
            further_input = self.__ask_if_further_input_needed()
            if further_input.strip().lower() == "ok":
                break
            # Refine the task description based on user input
            self.__refine_task_description(further_input) """