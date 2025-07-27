from sqlalchemy import select
from sqlalchemy.orm import joinedload

from infrastructure.adapters.database.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Album, Artist
from infrastructure.database.repositories.read_repository import ReadRepository


class ArtistReadRepository(ReadRepository[Artist]):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Artist)

    def _get_query(self) -> select:
        query = select(self._model).options(
            joinedload(self._model.albums).joinedload(Album.tracks)
        )
        return query
