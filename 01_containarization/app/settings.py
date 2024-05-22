from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret , default="sqlite:///./test.db")
# DATABASE_URL = config("DATABASE_URL", cast=Secret, default="sqlite:///mydatabase.db")

TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)
# TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret, default="sqlite:///test.db")