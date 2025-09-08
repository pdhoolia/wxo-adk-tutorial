import json
from typing import Optional, List

import requests
from pydantic import Field, BaseModel
import base64

from requests.auth import HTTPBasicAuth

from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from ibm_watsonx_orchestrate.run import connections

from ibm_watsonx_orchestrate.agent_builder.connections import ConnectionType


CONNECTION_SNOW = 'service-now'

class ServiceNowIncident(BaseModel):
    """
    Represents the details of a ServiceNow incident.
    """
    incident_number: str = Field(..., description='The incident number assigned by ServiceNow')
    short_description: str = Field(..., description='A brief summary of the incident')
    description: Optional[str] = Field(None, description='Detailed information about the incident')
    state: str = Field(..., description='Current state of the incident')
    urgency: str = Field(..., description='Urgency level of the incident')
    created_on: str = Field(..., description='The date and time the incident was created')

@tool(
    expected_credentials=[
        {"app_id": CONNECTION_SNOW, "type": ConnectionType.BASIC_AUTH}
    ]
)
def get_my_service_now_incidents() -> List[ServiceNowIncident]:
    """Fetches all ServiceNow incidents authored by the user.

    Returns:
        list[dict]: A list of incident details, including:
            - number (str): The incident number.
            - sys_id (str): The system ID of the incident.
            - description (str): The incident description.
            - state (str): The current state of the incident.
            - urgency (str): The urgency level of the incident.
    """
    creds = connections.basic_auth(CONNECTION_SNOW)
    base_url = creds.url
    url = f"{base_url}/api/now/table/incident"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    query_params = {}
    query_params['sys_created_by'] = 'admin'
    
    response = requests.get(
        url,
        headers=headers,
        params=query_params,
        auth=HTTPBasicAuth(creds.username, creds.password)
    )
    response.raise_for_status()
    data = response.json()['result']
    
    lst =  [ServiceNowIncident(
        incident_number=d['number'],
        short_description=d['short_description'],
        description=d.get('description', ''),
        state=d['state'],
        urgency=d['urgency'],
        created_on=d['opened_at']
    ) for d in data]
    lst.sort(key=lambda o: o.created_on, reverse=True)
    lst = lst[:min(len(lst), 10)]
    return lst

# if __name__ == '__main__':
#     incidents = get_my_service_now_incidents()
#     print(incidents)