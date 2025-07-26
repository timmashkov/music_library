from infrastructure.adapters.database.alchemy_adapter import AlchemyAdapter
from infrastructure.database.models import Track
from infrastructure.database.repositories.read_repository import ReadRepository


class TrackReadRepository(ReadRepository[Track]):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Track)
