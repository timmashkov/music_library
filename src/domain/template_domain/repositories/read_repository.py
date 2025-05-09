from typing import Optional

from adapters.database.alchemy_adapter import AlchemyAdapter
from domain.template_domain.interfaces.read_repository_interface import (
    TemplateReadRepositoryInterface,
)
from infrastructure.database.models import Template
from infrastructure.database.repositories.read_repository import ReadRepository


class TemplateReadRepository(ReadRepository, TemplateReadRepositoryInterface):

    def __init__(self, session_adapter: AlchemyAdapter) -> None:
        super().__init__(session_adapter, Template)

    async def find_user(self, login: str) -> Optional[Template]:
        async with self._session() as session:
            stmt = self.__get_query().where(self._model.login == login)
            answer = await session.execute(stmt)
        return answer.unique().scalar_one_or_none()
