# Customer Care Example

In this tutorial, we will simulate a customer care agent for a hospital. It is capable of querying remote APIs with dummy data. Key concepts demonstrated here include:
- integration with enterprise APIs using authentication credentials.

The following steps guide you thru this example.

1. In your directory, create a folder with the name `customer-care-agent`.
2. In this add folders `agents`, and `tools` to structure your agents and tools.
3. In the `agents` folder lets insert the following code into the `customer_care_agent.yaml` file

    ```yaml
    spec_version: v1
    style: react
    name: customer_care_agent
    llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
    description: |
        You are an agent who specializes in customer care for a large healthcare institution. You should be compassionate to the user.
        
        You are able to answer questions around benefits provided by different plans, the status of a claim,
        and are able to help direct people to the nearest provider for a particular ailment.
    instructions: >
        Use the search_healthcare_providers tool to search for providers. If more than 1 is returned format as a github formatted markdown table. Otherwise simply return the output in a kind conversational tone. Do not expand speciality acronyms.
        
        Use the get_healthcare_benefits tool to fetch the benefits coverage for a particular ailment, or for generic plan comparisons. Respond to get_healthcare_benefits requests in a github style formatted markdown table. Be specific about the expected coverage type if a particular condition is mentioned.
        
        Use the get_my_claims tool to fetch your open medical claims. Make sure to respond in a direct tone and do not negotiate prices. Format the output of get_my_claims as a github style markdown table.
    collaborators:
        - service_now_agent
    tools:
        - search_healthcare_providers
        - get_healthcare_benefits
        - get_my_claims
    ```

4. The above is our main agent. As you may notice, we've specified a collaborator agent for service now with it. Let's insert the following into `service_now_agent.yaml`.

    ```yaml
    spec_version: v1
    style: react
    name: service_now_agent
    llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
    description: >
        You are an agent who specializes in customer care for a large healthcare institution. You should be compassionate to the user.
        
        You are able to help help a user create tickets in service now for processing by a human later. Examples of when to do do this include for adding members to plans or helping users with documentation.
    instructions: >
        If a user is having difficulty either generating benefits documents or adding additional members to their plan, create a new incident for our support team using service_now_create_incident tool. Be compassionate about the user facing difficulty.
        
        The output of get_service_now_incidents should be formatted as a github style formatted markdown table.
    collaborators: []
    tools:
        - create_service_now_incident
        - get_my_service_now_incidents
        - get_service_now_incident_by_number
    ```

5. Let's now create the tools required by both of the agents above. We'll organize the tools in [customer_care](./tools/customer_care/) and [servicenow](./tools/servicenow/) folders.
6. We'll also add the libraries required by the tools in [requirements.txt](./tools/requirements.txt).

Now, before we import our agents and tools, we must setup a ServiceNow instance, and add an application integration to it in Orchestrate. Our `servicenow` tools will refer to that application integration to access the authentication details required. Here are the steps to setup a service-now instance.

1. Signup for a Sevice Now account at [https://developer.servicenow.com/dev.do](https://developer.servicenow.com/dev.do).
2. Validate your email address (Check your email)
3. On the landing page click **start building**. This will allocate a new instance of SNOW for you.
4. Once the instance has been provisioned, click on **manage instance**. This will show you your instance URL, as well as the `admin` user's password. Note those down.
5. Create an **application** connection using these credentials

    ```bash
    # create an application connection named service-now
    orchestrate connections add -a service-now

    # configure a draft environment for service-now app connection with draft environment URL
    orchestrate connections configure -a service-now --env draft --type team --kind basic --url <the instance url, something like: https://dev123456.service-now.com/>

    # set the credentials to access the draft environment for service-now application integration
    orchestrate connections set-credentials -a service-now --env draft -u admin -p <password you noted above>
    ```

Now we are ready to import the `servicenow` tools that need this application integration for authorized access to the servicenow API. E.g.,

```bash
# note the reference to the service-now application integration for the tool
orchestrate tools import -k python -f ./create_service_now_incident.py -r ./requirements.txt -a service-now
```

Also note how the tool accesses the application integration and its credentials. E.g., here's relevant snippet from [create_service_now_incident.py](./tools/servicenow/create_service_now_incident.py)

```python
...
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.agent_builder.connections import ConnectionType

CONNECTION_SNOW = 'service-now'
...

@tool(
    ...
    expected_credentials=[
        {"app_id": CONNECTION_SNOW, "type": ConnectionType.BASIC_AUTH}
    ]
)
def create_service_now_incident(
        short_description: str,
        description: str = None,
        urgency: int = 3
):
    ...
    creds = connections.basic_auth(CONNECTION_SNOW)
    base_url = creds.url
    ...
```

While we can one by one once again import all the tools and agents, this time we'll use this simple [import-all.sh](./import-all.sh) script to import all the tools and agents in our `customer-care-agent` folder. This expects `agents`, and `tools` folder, and a `tools/requirements.txt` file for any third party library dependency that the tools may have. It will recursively go thru all the sub-folders in tools, and import all the tools from all the files therein.

> ⚠️ If you see any issues while importing tools, one workaround may be to explicitly `uv pip install -r tools/requirements.txt` first.

**Try it out**  

- Show me my benefits related to mental health
- show me my open claims
- I need help to find a doctor for my son's ear pain, near Lowell

- I need help generating my benefits' documentation. Can you open a ticket.
- Can you get my open incident number
