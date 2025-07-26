from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import Base


class Genre(Base):

    title: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, comment="Genre's title"
    )

    description: Mapped[str | None] = mapped_column(Text, comment="Genre's description")
