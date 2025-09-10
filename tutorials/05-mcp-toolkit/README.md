# Using an MCP toolkit with your agent (No code)

In this tutorial we will add MCP tools from GitHub server to our agent.
We will use the reference implementation of a GitHub MCP server to demonstrate this.

```json
{
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
    }
}
```

Following steps guide us thru this.

* Create a GitHub personal access token. (If you don't have one already)
* Go to the **Manage > Connections** on Orchestrate dashboard
   ![Manage Connections](./images/01-manage-connection.jpg)
* Let's add a new connection
   ![Add new connection](./images/02-add-new-connection.jpg)
* Let's save and continue
   ![Save and continue](./images/03-save-and-continue.jpg)
* Now configure key-value type credentials for the draft | live environments as needed (and connect).
   ![Configure connection](./images/04-configure-connection.jpg)

---

We could just point select our SaaS environment, and import the MCP server toolkit using the CLI as below:

   ```bash
   # Set the environment
   orchestrate env activate my-saas

   # Import the toolkit
   orchestrate toolkits import \
     --kind=mcp \
     --name=mcp-github \
     --language=node \
     --description='All the Github tools' \
     --package='@modelcontextprotocol/server-github' \
     --command='npx -y @modelcontextprotocol/server-github' \
     --tools="*" \
     --app-id=github
   ```

---

Here's how to do this using the Orchestrate dashboard UI:

- Go to the **Agent Builder** on Orchestrate dashboard
   ![Agent Builder](./images/05-agent-builder.jpg)
- Let's **create a new agent from scratch** with the following details:
      - Name: github-agent
      - Description: An agent that interacts with GitHub repositories to do various GitHub activities like repo listing, issue management, commit listing etc.
- Let's now go to the **Toolset** section and click on **Add tool +** and **Import external**
   ![Add external Tools](./images/06-import-external.jpg)
- And then select the "Import from MCP server" option
   ![Import from MCP server](./images/07-import-from-mcp-server.jpg)
- Here let's **Add MCP server** with the following details:
   - Name: github
   - Description: Toolkit for GitHub MCP Server tools
   - Connection: github (the one we created earlier)
   - Install Command: `npx -y @modelcontextprotocol/server-github`

   ![Add MCP server](./images/08-add-mcp-server.jpg)
- You should see a Connection successful message if everything is fine.
   ![Connection Successful](./images/09-connection-successful.jpg)
- Now let's search and add `list_commits`
   ![Search and add list_commits](./images/10-add-mcp-tool.jpg)
- Similarly, let's add `list_repositories`

5. Try it out
   - List my (pdhoolia) "*tutorial" repositories
   ![Try It](./images/11-try-it.jpg)
   - List commits: List last 5 commits in my wxo-tutorial repo
