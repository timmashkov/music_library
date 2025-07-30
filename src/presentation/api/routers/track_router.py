from application.container import Container
from domain.track.entities.model import TrackFilter, TrackIncomingData, TrackResultData
from infrastructure.common.base_entities.base_router import BaseRouter


class TrackRouter(BaseRouter):
    prefix = "/track"
    tags = ["Track"]
    filters = TrackFilter
    service_client = Container.track_service
    input_model = TrackIncomingData
    output_model = TrackResultData

    def __init__(self) -> None:
        super().__init__()
        self._add_routes()
