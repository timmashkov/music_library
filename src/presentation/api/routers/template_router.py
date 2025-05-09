from typing import List, Union
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from pydantic import BaseModel

from application.services.template_service import TemplateService
from domain.template_domain.entities.model import (
    TemplateFilter,
    TemplateIncomingData,
    TemplateResultData,
)
from infrastructure.common.interfaces.router_interface import AbstractRouter


class TemplateRouter(AbstractRouter):
    api_router = APIRouter(prefix="/template", tags=["Template"])
    filters: TemplateFilter = FilterDepends(TemplateFilter)
    service_client: TemplateService = Depends(TemplateService)
    input_model: BaseModel = TemplateIncomingData
    output_model: BaseModel = TemplateResultData

    @staticmethod
    @api_router.get("/{uuid}", response_model=output_model)
    async def get_object(
        uuid: Union[str, UUID],
        order_provider: TemplateService = service_client,
    ) -> output_model:
        return await order_provider.get_item(uuid=uuid)

    @staticmethod
    @api_router.get("/", response_model=List[output_model])
    async def get_objects(
        order_provider: TemplateService = service_client,
        filters: filters = filters,
    ) -> List[output_model]:
        return await order_provider.get_items(filters=filters)

    @staticmethod
    @api_router.post("/", response_model=output_model)
    async def create_object(
        data: input_model,
        order_provider: TemplateService = service_client,
    ) -> output_model:
        return await order_provider.create_item(data=data)

    @staticmethod
    @api_router.patch("/{uuid}", response_model=output_model)
    async def update_object(
        uuid: Union[str, UUID],
        data: input_model,
        order_provider: TemplateService = service_client,
    ) -> output_model:
        return await order_provider.update_item(uuid=uuid, data=data)

    @staticmethod
    @api_router.delete("/{uuid}", response_model=output_model)
    async def delete_object(
        uuid: Union[str, UUID],
        order_provider: TemplateService = service_client,
    ) -> output_model:
        return await order_provider.delete_item(uuid=uuid)
