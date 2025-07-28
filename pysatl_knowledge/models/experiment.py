from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from pysatl_knowledge.models.base import Base


class Experiment(Base):
    """ORM model for experiments in the knowledge base."""

    __tablename__ = 'experiments'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    criterion_code: Mapped[str]
    sample_size: Mapped[int]
    iterations: Mapped[int]
    result: Mapped[float]
    status: Mapped[str] = mapped_column(default="pending")

    __table_args__ = (
        UniqueConstraint(
            "criterion_code",
            "sample_size",
            "iterations",
        ),
    )
