import datetime
from typing import Optional

from pydantic import BaseModel


class ReadersSchema(BaseModel):
    
    name: str
    age: int
    address: str
    email: str
    phone_number: Optional[int]
    joined_duration: datetime
    
    
class BooksSchema(BaseModel):
    
    title: str
    author: str
    ratings: Optional[int]
    qty_available: int
    genre: str
    available: bool = True
            
    
            
    
    
    