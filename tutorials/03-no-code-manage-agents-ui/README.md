# No-Code: Manage Agents UI

In this example we will create a simple agent using the tools and agents already available from previous examples. Unlike previous examples, we will not be writing any code. Instead, we will use the Orchestrate Chat UI to create and manage our agent. Key concepts demonstrated here are:
- Agent Builder UI
- Knowledge sources
- Ease of configuration (e.g., adding multi-lingual support)

We'll assume that you have already completed the previous tutorials and the agents and tools created there are available in your Orchestrate instance.

The following steps guide us thru this.

**Creating an Agent**

1. Launch the Orchestrate Chat UI by running the command `orchestrate chat start` in your terminal.
2. In the chat window, click on the **Manage Agents** button on the bottom left
3. You should be able to see your existing agents. Click on the **Create Agent** button.
4. Choose **Create from Scratch**.
5. Name your Agent, say, **Empower**. In the **Description**, insert text you prefer to describe the agent, say, “This agent’s role is to assist employees by answering their questions, providing guidance on supporting tickets, and service issues”.
6. Click **Create** to complete.

**Adding Knowledge**
1. In the Agent Builder UI, navigate to the **Knowledge** area.
2. Click on the **Choose Knowledge**.
3. Let's upload some knowledge files. Choose **Upload Files** and go **Next**.
4. Select the files you want to upload. We'll use the [policy documents here](./knowledge/) and go **Next**.
5. In the knowledge source description, let's add a description, say, “Health care plan policy documents.”
6. Click **Save**

**Adding Toolset**

1. Click on the **Add Agent** button to include any other agents that this agent can collaborate with.
2. Choose "Add from local instance".
3. Select the **customer_care_agent** and click **Add to agent**.

---

**Try it out!**  

Now that we have created our agent, let's try it out.

- What are the available healthcare policies? And can you help me understand their salient distinct features?

> 🚀 Check the reasoning to see how the Agent uses the knowledge tool. Also check the document chunks based on which the Agent is providing answers.

- I need help to find a doctor for my son's ear pain, near Lowell

> 🚀 Check the reasoning to see how the Agent delegates this to the customer_care_agent which uses an appropriate tool to find the information.

---

**Adding Multi-lingual Support**

Let's go to the **Behavior** section of our Agent configuration and add the following instructions: 

```
Make sure to communicate with the user by matching the language it uses to communicate with you and adapting names and terms as appropriate, and also translate column names and anything else when returning the information to the user.

Pay attention to the correct language adaptation of inputs and outputs, always returning the information to the user in the same language they are using to communicate with you.
```

Now, let's try asking a question in Hindi:

- मुझे अपने बेटे के कान दर्द के लिए लोवेल के पास एक डॉक्टर खोजने में मदद चाहिए।