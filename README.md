# Lambdas All The Way Down

A sample web app that makes a word cloud of animal baby names (kitten, pup, etc.)

- The web app implements a couple examples of Python's lambda functions.
- The instructions also provide guidance on deploying to Amazon's Lambda service.

#### Technology stack
- Python (2 or 3 will work, 2.7 or 3.6 required for AWS Lambda)
- Flask
- JQCloud jquery library for generating the word cloud

#### Dependencies
- Python
- pip
- virtualenv

## Installation
```shell
git clone https://github.com/m3brown/lambdas-all-the-way-down
cd lambdas-all-the-way-down
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Using the app

Open the following URL to see the default page: http://localhost:5000/

The app also accepts overrides for preferred animal name and suffx:

- http://localhost:5000/polliwog
- http://localhost:5000/cub/scout

## Deploying to AWS Lambda

To deploy to AWS Lambda, you'll need an AWS account with keypair credentials
available in your environment.  Place your credentials in the ~/.aws/credentials
directory:

```
[default]
aws_access_key_id = your-access-key-here
aws_secret_access_key = your-secret-access-key-here
```

Next, you'll want to install the [Zappa](https://github.com/Miserlou/Zappa) python library.

```shell
pip install zappa
```

Initializing zappa creates a settings file zappa_settings.json, which auto-detects
the Flask app configuration.

```shell
zappa init
```

Next, deploy the app to Lambda dev environment:

```shell
zappa deploy
```

After answering all the prompts (the defaults should be fine) the deployment
will provide a URL that you can use immediately.
