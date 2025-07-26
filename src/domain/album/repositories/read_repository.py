from infrastructure.adapters.database.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Album
from infrastructure.database.repositories.read_repository import ReadRepository


class AlbumReadRepository(ReadRepository[Album]):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Album)
