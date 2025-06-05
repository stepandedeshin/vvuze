from typing import Optional

from pydantic import BaseModel

    
class SGroupMembers(BaseModel):
    user_id: int
    group_id: int