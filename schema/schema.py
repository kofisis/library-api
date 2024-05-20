import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReadersSchema(BaseModel):
    
    id: int
    name: str
    age: int
    address: str
    city: str
    country: str
    postcode: int
    email: str
    phone_number: Optional[int] = Field(default=0)
    # joined_duration: datetime
    
    
class BooksSchema(BaseModel):
    
    id: int
    title: str
    author: str
    ratings: Optional[int]
    qty_available: int
    genre: str
    available: bool = True
            
    
            
    
    
    