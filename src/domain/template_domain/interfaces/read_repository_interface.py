from abc import abstractmethod
from typing import Any

from infrastructure.common.interfaces.repository_interfaces import (
    AbstractReadRepository,
)


class TemplateReadRepositoryInterface(AbstractReadRepository):

    @abstractmethod
    async def find_template(self, login: str) -> Any:
        pass
