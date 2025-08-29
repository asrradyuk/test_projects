from models.token import Token
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class TokenRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, token: Token):
        self.session.add(token)
        await self.session.commit()
        await self.session.refresh(token)
        return token

    async def get_all(self):
        result = await self.session.execute(select(Token))
        return result.scalars().all()