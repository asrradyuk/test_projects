from pydantic import BaseModel

class BalanceCreate(BaseModel):
    wallet_id: int
    amount: float

class BalanceRead(BaseModel):
    id: int
    wallet_id: int
    amount: float

    class Config:
        orm_mode = True