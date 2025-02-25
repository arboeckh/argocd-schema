from setuptools import setup, find_packages

setup(
    name="schema_migration",
    version="0.1",
    packages=find_packages(),
    install_requires=["sqlalchemy", "alembic", "psycopg2"],
)
