import typing
import uuid

from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.track.entities.enums import TrackFormat
from infrastructure.database.models.base import Base

if typing.TYPE_CHECKING:
    from infrastructure.database.models import Album


class Track(Base):

    title: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, comment="Track's title"
    )
    duration: Mapped[int] = mapped_column(
        Integer, nullable=False, comment="Track's duration"
    )
    audio_url: Mapped[str | None] = mapped_column(
        String, comment="Audio's url in minio"
    )
    bitrate: Mapped[str] = mapped_column(String, comment="Track's bitrate")
    format: Mapped[TrackFormat] = mapped_column(
        Enum(TrackFormat), comment="Track's format"
    )
    artist_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("artists.uuid"),
        nullable=False,
        index=True,
        comment="Artist's unique id",
    )
    album_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("albums.uuid"),
        nullable=False,
        index=True,
        comment="Album's unique id",
    )
    album: Mapped["Album"] = relationship(
        "Album",
        back_populates="tracks",
        lazy="noload",
    )
