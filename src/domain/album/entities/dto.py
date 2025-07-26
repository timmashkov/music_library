from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class TemplateCreateDTO:
    login: str


@dataclass(frozen=True)
class TemplateResultDTO(TemplateCreateDTO):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
