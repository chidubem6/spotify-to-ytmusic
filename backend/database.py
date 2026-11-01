import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Read backend/.env and copy each NAME=value line into this
# program's environment variables (skips any that are already set,
# e.g. on Render, where the dashboard sets them instead).
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# The engine: SQLAlchemy's one object that knows how to reach PostgreSQL.
# Creating it doesn't connect yet; it opens connections (through psycopg)
# only when some code actually talks to the database.
engine = create_engine(DATABASE_URL) 
