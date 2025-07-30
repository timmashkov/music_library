from application.config import settings
from application.use_cases.album_use_case import AlbumUseCase
from application.use_cases.artist_use_case import ArtistUseCase
from application.use_cases.track_use_case import TrackUseCase
from domain.album.repositories.read_repository import AlbumReadRepository
from domain.album.repositories.write_repository import AlbumWriteRepository
from domain.artist.repositories.read_repository import ArtistReadRepository
from domain.artist.repositories.write_repository import ArtistWriteRepository
from domain.track.repositories.read_repository import TrackReadRepository
from domain.track.repositories.write_repository import TrackWriteRepository
from infrastructure.adapters.database.alchemy_adapter import AlchemyAdapter
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

    track_read_repository = OnlyContainer(
        TrackReadRepository,
        session_adapter=alchemy_manager(),
    )

    track_write_repository = OnlyContainer(
        TrackWriteRepository,
        session_adapter=alchemy_manager(),
    )

    artist_service = OnlyContainer(
        ArtistUseCase,
        read_repository=artist_read_repository(),
        write_repository=artist_write_repository(),
    )

    album_service = OnlyContainer(
        AlbumUseCase,
        read_repository=album_read_repository(),
        write_repository=artist_write_repository(),
    )

    track_service = OnlyContainer(
        TrackUseCase,
        read_repository=track_read_repository(),
        write_repository=track_write_repository(),
    )
