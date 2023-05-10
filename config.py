import os
from dotenv import load_dotenv

# Load all env vars contained in .env file
load_dotenv()

# Assign supported .env variables

api_key = os.environ.get("OPENAI_API_KEY")