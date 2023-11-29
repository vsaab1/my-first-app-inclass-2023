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

ALPHAVANTAGE_API_KEY=""
MAILGUN_API_KEY=""
MAILGUN_SENDER_ADDRESS=""
MAILGUN_DOMAIN=""
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
python -m app/unemployment.py
python -m app/stocks.py
```
python app/mymod.py

# testing section

Run tests:

```sh
pytest
```

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file

export FLASK_APP=web_app
flask run




