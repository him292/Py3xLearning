# Env file - (dot.env)
# How do yoi store your passworkd/username in the framework
# pip install python-dotenv


from dotenv import load_dotenv
import os


def test_update_req():
    load_dotenv()  # this will run the .env file from within the project, wherever created
    url = os.getenv("URL")
    print(url)
