from typing import List

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..entities.measurement import Measurement


def get_router(template: Jinja2Templates):
    router = APIRouter()

    @router.get("/", response_model=List[Measurement], response_class=HTMLResponse)
    async def root(request: Request):
        return template.TemplateResponse(
            request=request, name="index.html"
        )

    return router
