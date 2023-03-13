"""Echo API."""
from {{cookiecutter.project_slug}}.web.gql.echo.mutation import Mutation
from {{cookiecutter.project_slug}}.web.gql.echo.query import Query

__all__ = ["Query", "Mutation"]
