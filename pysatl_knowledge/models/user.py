from sqlalchemy.orm import Mapped, mapped_column
from pysatl_knowledge.models.base import Base


class User(Base):
    """ORM model for users in the knowledge base."""

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
