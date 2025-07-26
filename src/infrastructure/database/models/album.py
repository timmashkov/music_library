import typing
import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import Base

if typing.TYPE_CHECKING:
    from infrastructure.database.models import Artist, Track


class Album(Base):

    title: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, comment="Album's title"
    )
    description: Mapped[str | None] = mapped_column(Text, comment="Album's description")
    cover_url: Mapped[str | None] = mapped_column(
        String, comment="Cover's url in minio"
    )
    release_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, comment="Release date"
    )
    artist_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("artists.uuid"),
        nullable=False,
        index=True,
        comment="Artist's unique id",
    )
    genre_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("genres.uuid"),
        nullable=True,
        index=True,
        comment="Artist's genre id",
    )

    artist: Mapped["Artist"] = relationship(
        "Artist",
        back_populates="albums",
        lazy="noload",
    )

    tracks: Mapped[typing.List["Track"]] = relationship(
        "Track",
        back_populates="album",
        cascade="all, delete-orphan",
        passive_updates=True,
        passive_deletes=True,
        lazy="noload",
    )
