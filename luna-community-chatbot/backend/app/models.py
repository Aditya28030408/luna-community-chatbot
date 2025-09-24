from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from .config import settings


engine = create_async_engine(settings.DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
pass


class Message(Base):
__tablename__ = "messages"
id: Mapped[int] = mapped_column(Integer, primary_key=True)
text: Mapped[str] = mapped_column(String(1024))
label: Mapped[str] = mapped_column(String(50))