#!/usr/bin/env bash
set -x

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Import all Python tools recursively from the tools folder
if [ -d "${SCRIPT_DIR}/tools" ]; then
  # Check if requirements.txt exists
  REQUIREMENTS_ARG=""
  if [ -f "${SCRIPT_DIR}/tools/requirements.txt" ]; then
    REQUIREMENTS_ARG="-r ${SCRIPT_DIR}/tools/requirements.txt"
  fi
  
  # Find all .py files recursively and import them
  find "${SCRIPT_DIR}/tools" -type f -name "*.py" | while read -r python_tool; do
    # Get relative path from tools directory
    relative_path="${python_tool#${SCRIPT_DIR}/tools/}"
    
    # Check if it's in a servicenow subdirectory for app-id
    if [[ "$relative_path" == servicenow/* ]]; then
      orchestrate tools import -k python -f "${python_tool}" ${REQUIREMENTS_ARG} --app-id service-now
    else
      orchestrate tools import -k python -f "${python_tool}" ${REQUIREMENTS_ARG}
    fi
  done
fi

# Import YAML agents from the agents folder. Since there is a dependency on service_now_agent, import it first.
for agent in service_now_agent.yaml customer_care_agent.yaml; do
  orchestrate agents import -f ${SCRIPT_DIR}/agents/${agent}
done