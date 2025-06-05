from typing import Optional

from pydantic import BaseModel

    
class SMessages(BaseModel):
    text: Optional[str] = None
    media_url: Optional[str] = None

