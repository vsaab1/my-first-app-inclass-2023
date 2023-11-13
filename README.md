# my-first-app-inclass-2023




## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```


Install packages:

```sh
pip install -r requirements.txt
```

Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="abc123"
MAILGUN_API_KEY="3a4873fedd47c51ba1e6fc047a5c6955-3e508ae1-3788de55"
MAILGUN_SENDER_ADDRESS="vs647@georgetown.edu"
MAILGUN_DOMAIN="sandboxb0f4d78ff35f4c468268744f9898f36b.mailgun.org"
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
python -m app/unemployment.py
```
python app/mymod.py

# testing section

Run tests:

```sh
pytest
```






