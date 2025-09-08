# IBM Watson Orchestrate ADK Developer Edition

watsonx Orchestrate Developer Edition runs as a local server on your computer, giving you a dedicated development environment. The ADK includes a CLI (command line interface) that helps you manage this local setup.

This has 2 main components:

- watsonx Orchestrate server: A local instance of watsonx Orchestrate that runs on your machine. It includes its own UI, API endpoints, and optional services such as observability using Langfuse.

- watsonx Orchestrate copilot server: A copilot assistant that helps you build and refine agents and tools.

The developer edition runs inside a Docker container, so you need to have Docker Engine installed on your machine. You may use any of the following:

- [Download & install Docker Desktop](https://docs.docker.com/get-docker/)
- Or [Download & install Rancher Desktop](https://github.com/rancher-sandbox/rancher-desktop/releases)

> 📌 If you use Rancher Desktop make sure to configure it using the [instructions here](https://github.com/IBM/ibm-watsonx-orchestrate-adk/blob/main/_docs/recommended-docker-settings/rancher-settings.md).

## Prerequisites

- **Hardware**: Minimum 16GB RAM (recommended 32 GB), and 8 CPU cores
- **Access**: You must have access to at least one of the following services:
  - watsonx Orchestrate
  - watsonx.ai
- **License**: watsonx Orchestrate Developer Edition license

## Install

**UV**:  
I recommend using `uv` to manage your virtual environments.  
You can install it via the following command:

```bash
# official installation script from https://astral.sh/uv/
curl -LsSf https://astral.sh/uv/install.sh | sh

# or via brew (macOS)
# brew install uv

# or via scoop (Windows)
# scoop install uv
```

**Environment**:  
Let's create a folder for our tutorial and a virtual environment for the ADK

```bash
mkdir wxo-tutorial
cd wxo-tutorial
uv venv
uv add ibm-watsonx-orchestrate
source .venv/bin/activate  # on Windows use `.venv\Scripts\activate`
```

**Config file**:  

To pull the ADK Docker images to run the developer edition locally, you need to create a `.env` file with the required authentication variables to pull the container images.

Official documentation suggests that you can do this **using watsonx Orchestrate service instance** on IBM Cloud as follows:

1. Go to your watsonx Orchestrate instance on IBM Cloud.
2. Click your user profile icon on the top right and select "Settings".
3. Go to the "API Details" tab.
4. If you don't already have an API Key on IBM Cloud, Click "Generate API key", create a new API key, and copy it.
5. Also copy the "Service Instance URL" from the same page.
6. Create a `.env` file in your `wxo-tutorial` folder with the following content:

```
WO_DEVELOPER_EDITION_SOURCE=orchestrate
WO_INSTANCE=<your service instance URL>  # as copied above
WO_API_KEY=<your API key>  # as copied above
```

However, very likely the above steps will result in an authorization required error for some of the images. This is because the ADK images are hosted in the IBM Entitled Registry, and you need an entitlement key to access them.

The following alternative works smoothly, **using your watsonx.ai service instance** as follows:

1. Access [My IBM](https://myibm.ibm.com/)
2. Click on **View Library** tile
3. Click **Add a new key +** (if you don't already have a key for container software in IBM entitled registry)
4. Copy the generated entitlement key
5. Create a `.env` file in your `wxo-tutorial` folder with the following content:

```
WO_DEVELOPER_EDITION_SOURCE=myibm
WO_ENTITLEMENT_KEY=<your entitlement key for ibm container registry>  # as copied above
WATSONX_APIKEY=<your api key for watsonx.ai>  # this is your apikey for watsonx.ai
WATSONX_SPACE_ID=<your space id for watsonx.ai>  # this is your space id for watsonx.ai
```

Make sure to replace the placeholder values with your actual keys.

**Install watsonx Orchestrate server**:

```bash
orchestrate server start -e .env
```

This command will pull the required Docker images and start the watsonx Orchestrate server on your local machine. The first time you run this command, it will take some time to download the images.

At the completion of this command you should see output like this:

```
[INFO] - Migration ran successfully.
[INFO] - Waiting for orchestrate server to be fully initialized and ready...
[INFO] - Orchestrate services initialized successfully
[INFO] - Creating config file at location "/Users/pdhoolia/.cache/orchestrate/credentials.yaml"
[DEBUG] - Setting default credentials data
[WARNING] - Failed to refresh local credentials, please run `orchestrate env activate local`
[INFO] - You can run `orchestrate env activate local` to set your environment or `orchestrate chat start` to start the UI service and begin chatting.
```

And the following should now be accessible in your browser:

- Open API documentation at [http://localhost:4321/docs](http://localhost:4321/docs)
- API Base URL at [http://localhost:4321/api/v1](http://localhost:4321/api/v1)


**Install orchestrate copilot server**:

```bash
orchestrate copilot start -e .env
```

You should see output like this:

```
[INFO] - Copilot Service started successfully.
[INFO] - Waiting for Copilot component to be initialized...
[INFO] - Copilot service successfully started
```

---
> 📌  Now that the images are downloaded, you should set `WO_DEVELOPER_EDITION_SKIP_LOGIN` environment variable to `true` to skip IBM Container Registry login next time you start the server.


> 👉 As the output above suggests, you should run `orchestrate env activate local` to activate local environment. The main purpose of the Developer Edition is to run our and test our agents locally. Activating the local environment will set the necessary environment variables to point to your local instance of watsonx Orchestrate for all subsequent CLI commands.


> ⚠️ After activating the local environment, you will again have to run: `orchestrate server start -e .env` for database containers to start.
---

