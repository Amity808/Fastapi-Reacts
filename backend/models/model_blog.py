from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import relationship

from .base_class import Base

class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    postDate = Column(String)
