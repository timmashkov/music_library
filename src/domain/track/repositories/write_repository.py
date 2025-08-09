from infrastructure.adapters.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Track
from infrastructure.database.repositories.write_repository import WriteRepository


class TrackWriteRepository(WriteRepository[Track]):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Track)
