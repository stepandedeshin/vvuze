from typing import Optional

from pydantic import BaseModel

    
class SFriends(BaseModel):
    user_from: int
    user_to: int