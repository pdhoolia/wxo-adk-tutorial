# Hello World

The following steps guide you to make you agent available on Agent builder.

1. In your directory, create a folder with the name hello-world.
2. Open a text editor, such as Visual Studio Code.
3. To create the agent, copy the following code:

    ```yaml
    spec_version: v1
    kind: native
    name: greeter
    description: An agent that greets you using the output from its tool
    instructions: Always run the tool "Greeting" when the user types Greeting in the chat. 
    llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
    style: default
    collaborators: []
    tools: 
    - greeting
    ```

4. Paste the code in the text editor and save the file as `greeter.yaml` in the `hello-world` folder.
5. To create the tool, copy the following code:

    ```python
    #greetings.py
    from ibm_watsonx_orchestrate.agent_builder.tools import tool


    @tool
    def greeting() -> str:
        """
        Greeting for everyone   
        """

        greeting = "Hello World"
        return greeting
    ```

6. Paste the code in the text editor and save the file as `greetings.py` in the `hello-world/tools` folder.
7. In the terminal go to the `hello-world` folder.
8. Run the command `orchestrate tools import -k python -f tools/greetings.py` . This will import our tool to the orchestrate servers tools registry, and make it available to any agent that may refer to it.
9. Run the command `orchestrate agents import -f greeter.yaml` . This will create or update the agent based on the specification in `greeter.yaml` file.
10. Run the command `orchestrate chat start` . This will start the Orchestrate Chat UI locally.
11. In the chat window enter something in the theme of "Greet me", and interact.
