from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    stack_id = Column(String, index=True)
    filename = Column(String)
