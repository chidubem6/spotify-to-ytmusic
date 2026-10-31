import os

from dotenv import load_dotenv

# Read backend/.env and copy each NAME=value line into this
# program's environment variables (skips any that are already set,
# e.g. on Render, where the dashboard sets them instead).
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
