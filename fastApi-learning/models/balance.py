from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import Integer, Float, ForeignKey
from database import Base 

class Balance(Base):
    __tablename__ = "balances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    amount: Mapped[float] = mapped_column(Float)

    wallet = relationship("Wallet", back_populates="balances")