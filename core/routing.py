from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLResolver,URLRouter
import chat.routing

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})