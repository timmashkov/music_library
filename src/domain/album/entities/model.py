import datetime
import uuid
from uuid import UUID

import pydantic

from infrastructure.common.base_entities.patched_filter import PatchedFilter
from infrastructure.database.models import Album


class AlbumIncomingData(pydantic.BaseModel):
    title: str = pydantic.Field(description=Album.title.comment)
    description: str | None = pydantic.Field(
        default_factory=str,
        description=Album.description.comment,
    )
    cover_url: str | None = pydantic.Field(
        default_factory=str,
        description=Album.cover_url.comment,
    )
    artist_uuid: UUID | None = pydantic.Field(
        default_factory=uuid.UUID,
        description=Album.artist_uuid.comment,
    )


class AlbumResultData(AlbumIncomingData):
    uuid: UUID = pydantic.Field(description=Album.uuid.comment)
    created_at: datetime.datetime = pydantic.Field(description=Album.created_at.comment)
    updated_at: datetime.datetime = pydantic.Field(description=Album.updated_at.comment)


class AlbumFilter(PatchedFilter):
    uuid: UUID | None = None
    title: str | None = None

    class Constants(PatchedFilter.Constants):
        model = Album
