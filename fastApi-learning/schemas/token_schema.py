from pydantic import BaseModel

class TokenCreate(BaseModel):
    symbol: str
    name: str

class TokenRead(TokenCreate):
    id: int
    class Config:
        orm_mode = True