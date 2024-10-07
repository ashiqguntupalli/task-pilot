import logging

class MemoryAgent:
    """
    An agent that keeps track of variables collected from other agents during the workflow.
    """

    def __init__(self, disable_logging=False):
        """
        Initialize the memory agent with an empty dictionary to store variables and a logger.
        """
        self.variables = {}
        self.logger = logging.getLogger('memory_agent')
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler('memory_agent.log')
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)
        self.logger.disabled = disable_logging

    def collect_variables(self, agent_name, variables):
        """
        Collect variables from another agent and store them in the memory.
        :param agent_name: The name of the agent providing the variables.
        :param variables: A dictionary of variables collected from the agent.
        """
        self.variables[agent_name] = variables

    def get_variables(self, agent_name=None):
        """
        Get the variables collected so far.
        :param agent_name: The name of the agent for which the variables are requested.
        :return: A dictionary of variables collected from the specified agent or all agents if no agent name is provided.
        """
        if agent_name:
            return self.variables.get(agent_name)
        return self.variables

    def log_message(self, message):
        """
        Log a message.
        :param message: The message to log.
        """
        self.logger.info(message)

    def log_error(self, error):
        """
        Log an error.
        :param error: The error to log.
        """
        self.logger.error(error)

