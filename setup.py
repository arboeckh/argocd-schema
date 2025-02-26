from setuptools import setup, find_packages

setup(
    name="schema",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=1.4",
        "alembic>=1.7",
        "psycopg2>=2.9",
        "dotenv>=0.19",
    ],
    python_requires=">=3.7",
)
