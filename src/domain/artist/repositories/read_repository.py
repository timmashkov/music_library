from sqlalchemy import select

from infrastructure.adapters.database.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Artist
from infrastructure.database.repositories.read_repository import ReadRepository


class ArtistReadRepository(ReadRepository[Artist]):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Artist)

    def _get_query(self) -> select:
        query = select(self._model).outerjoin(self._model.albums)
        return query
