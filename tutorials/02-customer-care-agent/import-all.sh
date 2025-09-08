#!/usr/bin/env bash
set -x

orchestrate env activate local
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

# Import all YAML agents from the agents folder
if [ -d "${SCRIPT_DIR}/agents" ]; then
  find "${SCRIPT_DIR}/agents" -type f -name "*.yaml" -o -name "*.yml" | while read -r agent; do
    orchestrate agents import -f "${agent}"
  done
fi