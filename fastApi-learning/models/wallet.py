from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import Integer, String
from database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)

    balances = relationship("Balance", back_populates="wallet")