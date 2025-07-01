import re
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "")

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_database_if_not_exists():
    """
    Connect to the server without a specific DB and create the database if missing.
    """
    # Extract DB name from DATABASE_URL (works for mysql+pymysql://user:pass@host/db)
    match = re.search(r"/([a-zA-Z0-9_]+)(?:\?.*)?$", DATABASE_URL)
    if not match:
        raise ValueError("Could not parse database name from DATABASE_URL")
    db_name = match.group(1)
    
    # Build URL without database
    base_url = re.sub(r"/[a-zA-Z0-9_]+(\?.*)?$", "/", DATABASE_URL)
    
    # Connect to server
    tmp_engine = create_engine(base_url, echo=True)
    with tmp_engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4;"))
