from application.config import settings
from application.server import ApiServer
from presentation.api.routers.album_router import AlbumRouter
from presentation.api.routers.artist_router import ArtistRouter
from presentation.api.routers.track_router import TrackRouter

music_library_app = ApiServer(
    name=settings.NAME,
    routers=[
        ArtistRouter().api_router,
        AlbumRouter().api_router,
        TrackRouter().api_router,
    ],
    start_callbacks=[],
    stop_callbacks=[],
).app
