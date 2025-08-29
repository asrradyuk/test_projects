from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from repositories.token_repository import TokenRepository
from models.token import Token
from schemas.token_schema import TokenCreate, TokenRead

router = APIRouter()

@router.post("/", response_model=TokenRead)
async def create_token(data: TokenCreate, db: AsyncSession = Depends(get_db)):
    repo = TokenRepository(db)
    token = Token(symbol=data.symbol, name=data.name)
    return await repo.create(token)

@router.get("/", response_model=list[TokenRead])
async def get_tokens(db: AsyncSession = Depends(get_db)):
    repo = TokenRepository(db)
    return await repo.get_all()