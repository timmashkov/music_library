from sqlalchemy import select
from sqlalchemy.orm import joinedload

from infrastructure.adapters.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Album
from infrastructure.database.repositories.read_repository import ReadRepository


class AlbumReadRepository(ReadRepository[Album]):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Album)

    def _get_query(self) -> select:
        query = select(self._model).options(joinedload(self._model.tracks))
        return query
