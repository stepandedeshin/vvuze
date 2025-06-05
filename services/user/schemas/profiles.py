from typing import Optional

from pydantic import BaseModel

    
class SProfiles(BaseModel):
    first_name: str
    last_name: str
    picture_url: Optional[str] = None
    bio: Optional[str] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    


    