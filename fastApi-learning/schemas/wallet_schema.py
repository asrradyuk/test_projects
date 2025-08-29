from pydantic import BaseModel

class WalletCreate(BaseModel):
    name: str

class WalletRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True