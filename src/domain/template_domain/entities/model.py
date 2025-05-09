from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from infrastructure.common.base_entities.patched_filter import PatchedFilter
from infrastructure.database.models import Template


class TemplateIncomingData(BaseModel):
    login: str = Field(description=Template.login.comment)


class TemplateResultData(TemplateIncomingData):
    uuid: UUID = Field(description=Template.uuid.comment)
    created_at: datetime = Field(description=Template.created_at.comment)
    updated_at: datetime = Field(description=Template.updated_at.comment)


class TemplateFilter(PatchedFilter):
    uuid: Optional[UUID] = None

    class Constants(PatchedFilter.Constants):
        model = Template
