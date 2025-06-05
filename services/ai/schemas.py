from pydantic import BaseModel


class SRequest(BaseModel):
    text: str