from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from typing import Any
class SPAService(StaticFiles):
    async def get_response(self, path: str, scope: Any) -> Response:
        response = await super().get_response(path, scope)
        if response.status_code == 404:
            response = await super().get_response("index.html", scope)
        return response