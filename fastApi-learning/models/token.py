from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    symbol: Mapped[str]
    name: Mapped[str]
    balances = relationship("Balance", back_populates="token")