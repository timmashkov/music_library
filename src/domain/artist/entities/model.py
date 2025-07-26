import datetime
from uuid import UUID

import pydantic

from infrastructure.common.base_entities.patched_filter import PatchedFilter
from infrastructure.database.models import Artist


class ArtistIncomingData(pydantic.BaseModel):
    name: str = pydantic.Field(description=Artist.name.comment)
    bio: str | None = pydantic.Field(
        default_factory=str, description=Artist.bio.comment
    )
    image_url: str | None = pydantic.Field(
        default_factory=str, description=Artist.image_url.comment
    )


class ArtistResultData(ArtistIncomingData):
    uuid: UUID = pydantic.Field(description=Artist.uuid.comment)
    created_at: datetime.datetime = pydantic.Field(
        description=Artist.created_at.comment
    )
    updated_at: datetime.datetime = pydantic.Field(
        description=Artist.updated_at.comment
    )


class ArtistFilter(PatchedFilter):
    uuid: UUID | None = None
    name: str | None = None

    class Constants(PatchedFilter.Constants):
        model = Artist
