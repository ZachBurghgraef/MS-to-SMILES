# Setup the python uv environment

## Install uv

Follow the instructions at the [link](https://docs.astral.sh/uv/getting-started/installation/) to download and install uv to manage your project.

## Setup uv for this project

Run the following commands in the project root:

```
uv sync
```

## Set up kaggle api

* Go to your Kaggle account settings [https://www.kaggle.com/settings/account](https://www.kaggle.com/settings/account)

* Scroll down and click "Create New API Token"

* This downloads a kaggle.json file with your API credentials

* Place the kaggle.json file in the correct location:

    * Linux/macOS: ~/.kaggle/kaggle.json

    * Windows: C:\Users\<YourUsername>\.kaggle\kaggle.json

* Set proper permissions on Linux/macOS:

        chmod 600 ~/.kaggle/kaggle.json


## Run the setup script

From root run:

```
uv run setup/setup.py
```