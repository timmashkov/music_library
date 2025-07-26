from application.config import settings
from application.server import ApiServer
from presentation.api.routers.template_router import TemplateRouter

music_library_app = ApiServer(
    name=settings.NAME,
    routers=[TemplateRouter().api_router],
    start_callbacks=[],
    stop_callbacks=[],
).app
