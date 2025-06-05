from typing import Optional

from pydantic import BaseModel

    
class SMessages(BaseModel):
    user_from: int
    user_to: int
    text: Optional[str] = None
    media_url: Optional[str] = None

