from typing import Optional

from pydantic import BaseModel

    
class SPosts(BaseModel):
    user_id: int
    content: Optional[str] = None
    media: Optional[str] = None


