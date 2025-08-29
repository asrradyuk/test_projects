from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.wallet import Wallet
from typing import List

class WalletRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, wallet: Wallet) -> Wallet:
        self.session.add(wallet)
        await self.session.commit()
        await self.session.refresh(wallet)
        return wallet

    async def get_all(self) -> List[Wallet]:
        result = await self.session.execute(select(Wallet))
        return result.scalars().all()