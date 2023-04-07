from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class BlogBase(BaseModel):
    title: str
    body: str
    postDate: Optional[datetime]










