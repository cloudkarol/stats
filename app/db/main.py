import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_db_url():
    username = os.getenv('DATABASE_USERNAME', 'postgres')
    password = os.getenv('DATABASE_PASSWORD', 'password')
    host = os.getenv('DATABASE_HOST', 'localhost')
    port = os.getenv('DATABASE_PORT', '5432')
    return f'postgresql://{username}:{password}@{host}:{port}/stats'

DATABASE_URL = get_db_url()
engine = create_engine(DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
