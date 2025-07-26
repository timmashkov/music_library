from adapters.database.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Artist
from infrastructure.database.repositories.read_repository import ReadRepository


class ArtistReadRepository(ReadRepository):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Artist)
