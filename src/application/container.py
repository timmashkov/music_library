from adapters.database.alchemy_adapter import AlchemyAdapter
from application.config import settings
from domain.artist.repositories.read_repository import ArtistReadRepository
from domain.artist.repositories.write_repository import ArtistWriteRepository
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

    artist_read_repository = OnlyContainer(
        ArtistReadRepository,
        session_adapter=alchemy_manager(),
    )

    artist_write_repository = OnlyContainer(
        ArtistWriteRepository,
        session_adapter=alchemy_manager(),
    )
