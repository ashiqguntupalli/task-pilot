# task-pilot

## 1. What is task-copilot?

Task-copilot is an intelligent task management and planning system that uses a series of specialized AI agents to help users break down complex tasks into manageable steps. It's designed to assist in task planning, requirement gathering, and task structuring by leveraging artificial intelligence to guide users through the process of defining and organizing their work.

## 2. How is this implemented?

The system is implemented using a modular architecture with multiple specialized agents, each responsible for a specific aspect of the task planning process. These agents are implemented in Python and work together in a sequential workflow. The system uses a shared memory component to pass information between agents and maintain the state of the task throughout the process.

The implementation relies on natural language processing and generation capabilities, likely provided by a language model (LLM) to interpret user inputs and generate appropriate responses and suggestions.

## 3. What is the role of every agent?

The task-copilot system consists of five main agents, each with a specific role in the task planning process:

1. Initializer Agent:
   - Responsible for starting the workflow and collecting initial information from the user.
   - Gathers the task subject and the module it falls under.
   - Sets the foundation for the subsequent agents to build upon.

2. Task Scope Agent:
   - Focuses on defining the high-level scope and complexity of the task.
   - Frames and asks questions to gather information about the task's overall scope.
   - Summarizes the collected information to create a clear task scope.

3. Requirements Agent:
   - Dives deeper into the specific requirements of the task.
   - Generates and asks detailed questions based on the task scope.
   - Collects and processes user responses to create a comprehensive list of requirements.

4. Structuring Agent:
   - Takes the high-level scope and detailed requirements as input.
   - Creates a structured task breakdown.
   - Organizes the task into logical components or subtasks.

5. Refinement Agent: (**Work in Progress**)
   - Reviews the generated task structure with the user.
   - Allows for iterative refinement of the task description.
   - Incorporates user feedback to improve and finalize the task structure.

## 4. How do these agents work in sequence (i.e., Recipe)?

The agents work in a predefined sequence, forming a recipe for task planning:

1. The Initializer Agent starts the process by collecting the basic task information from the user.

2. This information is passed to the Task Scope Agent, which uses it to frame relevant questions about the task's scope and complexity.

3. Once the scope is defined, the Requirements Agent takes over, using the scope information to generate more specific questions about the task's requirements.

4. With both the scope and detailed requirements in hand, the Structuring Agent creates a logical breakdown of the task into subtasks or components.

5. Finally, the Refinement Agent presents the structured task to the user, allowing for feedback and iterative improvements.

This sequence ensures that the task is progressively defined, from a high-level concept to a detailed, structured plan.

## 5. How do all agents share information?

The agents share information through a centralized memory component. This memory system allows for:

- Persistent storage of collected data throughout the workflow.
- Passing of information between agents without direct coupling.
- Maintaining the evolving state of the task planning process.

Each agent can:
- Retrieve information collected by previous agents.
- Store new information or modifications for use by subsequent agents.
- Log messages and track the progress of the workflow.

The memory component likely uses a key-value store or a similar structure to organize data, with each agent having designated variables or sections to read from and write to. This shared memory approach ensures that all agents work with consistent, up-to-date information throughout the task planning process.

By using this shared memory system, the task-copilot can maintain context across different stages of the planning process, allowing for a cohesive and integrated approach to task management and structuring.

## 6. Usage

Task-pilot can be run from the command line with various options. Here are the available input parameters:

- `-m` or `--model`: Specify the LLM model to use. Default is "llama3.2:3b".
- `-l` or `--log`: Enable logging. If not specified, logging is disabled by default.

### Prerequisites

Before running task-pilot, ensure that:

1. You have Python installed on your system.
2. Ollama is installed and running in the background.
3. The LLM model you intend to use is available in Ollama. For example, if you plan to use "llama3.2:3b", make sure it's pulled and ready in Ollama.

To start Ollama with a specific model, use: `ollama run <model_name>`
Replace `<model_name>` with the model you want to use (e.g., llama3.2:3b, deepseek-coder, etc.).

### Examples

1. Run task-pilot with default settings (logging disabled and model is llama3.2:3b): `python main.py`
2. Run task-pilot with ollama compatible model and logging enabled: `python main.py -m deepseek-coder -l`
3. Run task-pilot with ollama compatible model and logging disabled: `python main.py -m deepseek-coder`