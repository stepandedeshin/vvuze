from typing import Optional

from pydantic import BaseModel

    
class SLikes(BaseModel):
    user_id: int
    post_id: int

