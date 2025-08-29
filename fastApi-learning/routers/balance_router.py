from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.balance_repository import BalanceRepository
from database import get_session
from schemas.balance_schema import BalanceCreate, BalanceRead
from typing import List
from models.balance import Balance

router = APIRouter(prefix="/balances", tags=["balances"])

@router.post("/", response_model=BalanceRead)
async def create_balance(data: BalanceCreate, session: AsyncSession = Depends(get_session)):
    repo = BalanceRepository(session)
    new_balance = Balance(wallet_id=data.wallet_id, amount=data.amount)
    return await repo.add(new_balance)

@router.get("/", response_model=List[BalanceRead])
async def read_balances(session: AsyncSession = Depends(get_session)):
    repo = BalanceRepository(session)
    return await repo.get_all()