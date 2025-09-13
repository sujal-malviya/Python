from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "mysql+pymysql://root:root@localhost:3306/sujal"

engine = create_engine(database_url,pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind= engine)

Base = declarative_base()