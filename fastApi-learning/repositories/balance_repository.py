from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.balance import Balance
from typing import List

class BalanceRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, balance: Balance) -> Balance:
        self.session.add(balance)
        await self.session.commit()
        await self.session.refresh(balance)
        return balance

    async def get_all(self) -> List[Balance]:
        result = await self.session.execute(select(Balance))
        return result.scalars().all()