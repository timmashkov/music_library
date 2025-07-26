import typing
from infrastructure.database.models.base import Base
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

if typing.TYPE_CHECKING:
    from infrastructure.database.models import Album

class Artist(Base):

    name: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, comment="Artist's name"
    )
    bio: Mapped[str | None] = mapped_column(Text, comment="Artist's biography")
    image_url: Mapped[str | None] = mapped_column(
        String, comment="Image's url in minio"
    )

    albums: Mapped[typing.List["Album"]] = relationship(
        "Album",
        back_populates="artist",
        cascade="all, delete-orphan",
        passive_updates=True,
        passive_deletes=True,
        lazy="noload",
    )
