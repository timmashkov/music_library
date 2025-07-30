from application.container import Container
from domain.album.entities.model import AlbumFilter, AlbumIncomingData, AlbumResultData
from infrastructure.common.base_entities.base_router import BaseRouter


class AlbumRouter(BaseRouter):
    prefix = "/album"
    tags = ["Album"]
    filters = AlbumFilter
    service_client = Container.album_service
    input_model = AlbumIncomingData
    output_model = AlbumResultData

    def __init__(self) -> None:
        super().__init__()
        self._add_routes()
