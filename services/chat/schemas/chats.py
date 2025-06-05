from typing import Optional

from pydantic import BaseModel

    
class SChats(BaseModel):
    id: int
    user_from: int
    user_to: int

