import typing
import uuid

from fastapi import Depends

from application.container import Container
from domain.artist.entities.model import ArtistIncomingData
from infrastructure.common.base_entities.singleton import Singleton
from infrastructure.common.interfaces.repository_interfaces import (
    AbstractReadRepository,
    AbstractWriteRepository,
)
from infrastructure.database.models import Track


class TrackService(Singleton):
    def __init__(
        self,
        read_repository: AbstractReadRepository = Depends(
            Container.track_read_repository
        ),
        write_repository: AbstractWriteRepository = Depends(
            Container.track_write_repository
        ),
    ) -> None:
        self.read_repository = read_repository
        self.write_repository = write_repository

    async def get_item(self, uuid: str | uuid.UUID) -> Track | None:
        return await self.read_repository.get_item(uuid=uuid)

    async def get_items(self, filters: typing.Any = None) -> typing.List[Track]:
        return await self.read_repository.find(filters=filters)

    async def create_item(self, data: ArtistIncomingData) -> Track | None:
        return await self.write_repository.create_item(**data.model_dump())

    async def update_item(
        self, uuid: str | uuid.UUID, data: ArtistIncomingData
    ) -> Track | None:
        intel = data.model_dump()
        intel["uuid"] = uuid
        return await self.write_repository.update_item(**intel)

    async def delete_item(self, uuid: str | uuid.UUID) -> Track | None:
        return await self.write_repository.delete_item(uuid=uuid)
