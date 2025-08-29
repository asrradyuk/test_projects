from fastapi import FastAPI
from routers.wallet_router import router as wallet_router
from routers.balance_router import router as balance_router
from database import engine, Base

app = FastAPI()

app.include_router(wallet_router)
app.include_router(balance_router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)