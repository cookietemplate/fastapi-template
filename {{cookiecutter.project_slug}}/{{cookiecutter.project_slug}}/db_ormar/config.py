from databases import Database

from {{cookiecutter.project_slug}}.settings import settings

database = Database(str(settings.db_url))
