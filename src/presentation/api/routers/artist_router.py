from application.container import Container
from domain.artist.entities.model import (
    ArtistFilter,
    ArtistIncomingData,
    ArtistResultData,
)
from infrastructure.common.base_entities.base_router import BaseRouter


class ArtistRouter(BaseRouter):
    prefix = "/artist"
    tags = ["Artist"]
    filters = ArtistFilter
    service_client = Container.artist_service
    input_model = ArtistIncomingData
    output_model = ArtistResultData

    def __init__(self) -> None:
        super().__init__()
        self._add_routes()
