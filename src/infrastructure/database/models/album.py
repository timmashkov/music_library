import uuid
import typing

from infrastructure.database.models.base import Base
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if typing.TYPE_CHECKING:
    from infrastructure.database.models import Artist

class Album(Base):

    title: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, comment="Album's title"
    )
    description: Mapped[str | None] = mapped_column(Text, comment="Album's description")
    cover_url: Mapped[str | None] = mapped_column(
        String, comment="Cover's url in minio"
    )
    artist_uuid: Mapped[uuid.UUID] = mapped_column(ForeignKey("artists.uuid"), unique=True, nullable=False, index=True, comment="Artist's unique id")

    artist: Mapped["Artist"] = relationship(
        "Artist",
        back_populates="albums",
        lazy="noload",
    )
