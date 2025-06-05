from typing import Optional

from pydantic import BaseModel

    
class SGroups(BaseModel):
    name: str
    creator_id: int
    description: Optional[str] = None
