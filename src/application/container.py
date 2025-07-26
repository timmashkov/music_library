from application.config import settings

from adapters.database.alchemy_adapter import AlchemyAdapter
from domain.template_domain.repositories.read_repository import TemplateReadRepository
from domain.template_domain.repositories.write_repository import TemplateWriteRepository
from infrastructure.common.base_entities.singleton import OnlyContainer, Singleton


class Container(Singleton):

    alchemy_manager = OnlyContainer(
        AlchemyAdapter,
        dialect=settings.POSTGRES.dialect,
        host=settings.POSTGRES.host,
        login=settings.POSTGRES.login,
        password=settings.POSTGRES.password,
        port=settings.POSTGRES.port,
        database=settings.POSTGRES.database,
        echo=settings.POSTGRES.echo,
    )

    template_read_manager = OnlyContainer(
        TemplateReadRepository,
        session_adapter=alchemy_manager(),
    )

    template_write_manager = OnlyContainer(
        TemplateWriteRepository,
        session_adapter=alchemy_manager(),
    )
