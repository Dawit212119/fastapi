from typing import AsyncGenerator

import uuid

from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql  import UUID

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_sessionmaker

from sqlalchemy.orm  import DeclarativeBase, relationship
import datetime

DATABASE_URL="sqlite+aiosqlite:///./test.db"
class Base(DeclarativeBase):
     pass

class Post(Base):
    __tablename__="posts"

    id= Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    caption= Column(Text)
    url=Column(String,nullable=False)
    file_type=Column(String,nullable=False)
    file_name=Column(String,nullable=False)
    created_at= Column(DateTime,default=datetime.utcnow)

engine = create_async_engine(DATABASE_URL)      #  create asybc db engine
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)   #  create a session favtory for making db session



  # it will start the engine and create a sql table by reading the model from the orm  
async def create_db_and_tables():
    async with engine.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
#   it will start the session  so, can read and write data from/to db
async def  get_async_session() -> AsyncGenerator[AsyncSession,None]:
     async with async_session_maker() as session:
          yield session