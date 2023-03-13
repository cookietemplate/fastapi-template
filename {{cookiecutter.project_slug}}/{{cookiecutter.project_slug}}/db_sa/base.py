from sqlalchemy.orm import  DeclarativeBase

from {{cookiecutter.project_slug}}.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta

