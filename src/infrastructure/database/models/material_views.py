from sqlalchemy import func, select

from infrastructure.database.models import Album, Artist, Track
from infrastructure.database.models.base import Base, MatViewBase
from infrastructure.database.models.base_mat_view import create_mat_view


class ArtistAlbumsCount(MatViewBase):

    __table__ = create_mat_view(
        Base.metadata,
        "artist_album_count",
        select(
            Artist.uuid.label("artist_uuid"),
            func.count(Album.uuid).label("album_count"),
        )
        .select_from(Album)
        .join(Artist, Album.artist_uuid == Artist.uuid)
        .group_by(Artist.uuid),
    )


class AlbumTracksCount(MatViewBase):

    __table__ = create_mat_view(
        Base.metadata,
        "album_track_count",
        select(
            Album.uuid.label("album_uuid"), func.count(Track.uuid).label("track_count")
        )
        .select_from(Track)
        .join(Album, Track.album_uuid == Album.uuid)
        .group_by(Album.uuid),
    )
