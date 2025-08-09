from infrastructure.adapters.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Artist
from infrastructure.database.repositories.write_repository import WriteRepository


class ArtistWriteRepository(WriteRepository[Artist]):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Artist)
