# Using an MCP toolkit with your agent

In this tutorial we will see how to use an MCP toolkit with your agent. We will use the reference implementation of a GitHub MCP server to demonstrate this.

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

1. Create a GitHub personal access token.
2. Create a new application connection for github app, env: draft, kind: bearer

   ```bash
   # create an application connection named github
   orchestrate connections add -a github

   # configure a draft environment for github app connection with bearer type
   orchestrate connections configure -a github --env draft --type team --kind key_value


   # set credentials for github app connection in draft environment
   orchestrate connections set-credentials -a github --env draft -e GITHUB_PERSONAL_ACCESS_TOKEN=<YOUR_TOKEN>
   ```

3. Now import the toolkit

   ```bash
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

4. Now let's follow the earlier tutorial on [no-code agent creation](../03-no-code-manage-agents-ui/README.md) to create an agent with tools from this toolkit.
   - Start the agent builder ui

      ```bash
      orchestrate chat start
      ```
   - And let's create a new agent from scratch:
      - Name: github-agent
      - Description: An agent that interacts with GitHub repositories to do various GitHub activities like repo listing, issue management, commit listing etc.
      - Toolset:
         - Tools: let's search for mcp-github and select all the tools from this toolkit.

5. Try it out
   - List all my repositories
   - List commits: List last 5 commits in my wxo-tutorial repo
