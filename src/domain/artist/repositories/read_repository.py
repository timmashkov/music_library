from sqlalchemy import select
from sqlalchemy.orm import joinedload, with_expression

from infrastructure.adapters.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Album, Artist, ArtistAlbumsCount
from infrastructure.database.repositories.read_repository import ReadRepository


class ArtistReadRepository(ReadRepository[Artist]):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Artist)

    def _get_query(self) -> select:
        query = select(self._model).options(
            joinedload(self._model.albums).joinedload(
                Album.tracks
            )  # TODO: add optional join
        )
        query = query.outerjoin(
            ArtistAlbumsCount, self._model.uuid == ArtistAlbumsCount.artist_uuid
        ).options(
            with_expression(self._model.albums_count, ArtistAlbumsCount.album_count)
        )
        return query
