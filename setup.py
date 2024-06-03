from setuptools import find_packages, setup

setup(
    name="leave_mgmt",
    version="0.0.1",
    description="Leave Management Data Pipeline",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "SQLAlchemy==1.4.25",
        "python-dotenv==0.19.0",
        "psycopg2-binary==2.9.1",
        "loguru==0.5.3",
        "pydantic==1.8.2",
        "requests==2.26.0",
        "alembic==1.7.3",
        "SQLAlchemy-Utils==0.37.8",
        "aiohttp==3.9.5",
    ],
    python_requires=">=3.10",
)
