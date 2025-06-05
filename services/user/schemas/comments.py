from typing import Optional

from pydantic import BaseModel

    
class SComments(BaseModel):
    user_id: int
    post_id: int
    text: Optional[str] = None
    media_url: Optional[str] = None