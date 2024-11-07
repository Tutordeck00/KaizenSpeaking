import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

environment = os.getenv("ENVIRONMENT", "local")

if environment == "development":
    load_dotenv(".env.development", override=True)
    print("Loaded .env.development")
else:
    load_dotenv(".env.local", override=True)
    print("Loaded .env.local")

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Using DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
