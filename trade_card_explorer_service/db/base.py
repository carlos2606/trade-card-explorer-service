from sqlalchemy.orm import DeclarativeBase

from trade_card_explorer_service.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
