import typing
import uuid

import fastapi
import fastapi_filter
import pydantic

from application.services.track_service import TrackService
from domain.track.entities.model import TrackFilter, TrackIncomingData, TrackResultData
from infrastructure.common.interfaces.router_interface import AbstractRouter


class TrackRouter(AbstractRouter):
    api_router = fastapi.APIRouter(prefix="/track", tags=["Track"])
    filters: TrackFilter = fastapi_filter.FilterDepends(TrackFilter)
    service_client: TrackService = fastapi.Depends(TrackService)
    input_model: pydantic.BaseModel = TrackIncomingData
    output_model: pydantic.BaseModel = TrackResultData

    @staticmethod
    @api_router.get("/{uuid}", response_model=output_model)
    async def get_object(
        uuid: str | uuid.UUID,
        order_provider: service_client = service_client,
    ) -> output_model:
        return await order_provider.get_item(uuid=uuid)

    @staticmethod
    @api_router.get("/", response_model=typing.List[output_model])
    async def get_objects(
        order_provider: service_client = service_client,
        filters: filters = filters,
    ) -> typing.List[output_model]:
        return await order_provider.get_items(filters=filters)

    @staticmethod
    @api_router.post("/", response_model=output_model)
    async def create_object(
        data: input_model,
        order_provider: service_client = service_client,
    ) -> output_model:
        return await order_provider.create_item(data=data)

    @staticmethod
    @api_router.patch("/{uuid}", response_model=output_model)
    async def update_object(
        uuid: str | uuid.UUID,
        data: input_model,
        order_provider: service_client = service_client,
    ) -> output_model:
        return await order_provider.update_item(uuid=uuid, data=data)

    @staticmethod
    @api_router.delete("/{uuid}", response_model=output_model)
    async def delete_object(
        uuid: str | uuid.UUID,
        order_provider: service_client = service_client,
    ) -> output_model:
        return await order_provider.delete_item(uuid=uuid)
