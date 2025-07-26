from adapters.database.alchemy_adapter import AlchemyAdapter
from application.config import settings
from domain.album.repositories.read_repository import AlbumReadRepository
from domain.album.repositories.write_repository import AlbumWriteRepository
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

    album_read_repository = OnlyContainer(
        AlbumReadRepository,
        session_adapter=alchemy_manager(),
    )

    album_write_repository = OnlyContainer(
        AlbumWriteRepository,
        session_adapter=alchemy_manager(),
    )
