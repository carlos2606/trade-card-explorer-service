from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from trade_card_explorer_service.web.api.router import api_router
from trade_card_explorer_service.web.gql.router import gql_router
from trade_card_explorer_service.web.lifetime import (
    register_shutdown_event,
    register_startup_event,
)


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="trade_card_explorer_service",
        version=metadata.version("trade_card_explorer_service"),
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")
    # Graphql router
    app.include_router(router=gql_router, prefix="/graphql")

    return app
