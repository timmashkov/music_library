from application.config import settings
from application.server import ApiServer
from presentation.api.routers.artist_router import ArtistRouter

music_library_app = ApiServer(
    name=settings.NAME,
    routers=[ArtistRouter().api_router],
    start_callbacks=[],
    stop_callbacks=[],
).app
