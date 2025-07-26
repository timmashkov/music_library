import datetime
from uuid import UUID

import pydantic

from domain.track.entities.enums import TrackFormat
from infrastructure.common.base_entities.patched_filter import PatchedFilter
from infrastructure.database.models import Track


class TrackIncomingData(pydantic.BaseModel):
    title: str = pydantic.Field(description=Track.title.comment)
    duration: int = pydantic.Field(description=Track.duration.comment)
    audio_url: str | None = pydantic.Field(
        default_factory=str, description=Track.audio_url.comment
    )
    bitrate: str = pydantic.Field(description=Track.bitrate.comment)
    format: TrackFormat = pydantic.Field(description=Track.format.comment)
    artist_uuid: UUID | None = pydantic.Field(
        default_factory=UUID,
        description=Track.artist_uuid.comment,
    )
    album_uuid: UUID | None = pydantic.Field(
        default_factory=UUID,
        description=Track.album_uuid.comment,
    )


class TrackResultData(TrackIncomingData):
    uuid: UUID = pydantic.Field(description=Track.uuid.comment)
    created_at: datetime.datetime = pydantic.Field(description=Track.created_at.comment)
    updated_at: datetime.datetime = pydantic.Field(description=Track.updated_at.comment)


class TrackFilter(PatchedFilter):
    uuid: UUID | None = None
    title: str | None = None

    class Constants(PatchedFilter.Constants):
        model = Track
