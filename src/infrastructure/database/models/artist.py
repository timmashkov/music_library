from infrastructure.database.models import Base
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Artist(Base):

    name: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, comment="Artist's name"
    )
    bio: Mapped[str | None] = mapped_column(Text, comment="Artist's biography")
    image_url: Mapped[str | None] = mapped_column(
        String, comment="Image's url in minio"
    )
