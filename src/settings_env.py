from pydantic import BaseModel, SecretStr, Field, ConfigDict, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DjangoSettings(BaseModel):
    """
    Django application configuration including secret key, debug flag
    and the list of allowed hosts loaded from environment variables.
    """
    SECRET_KEY: SecretStr = Field(min_length=1)
    DEBUG: bool = True
    ALLOWED_HOSTS: list[str] = ["127.0.0.1", "localhost"]

    model_config = ConfigDict(
        use_attribute_docstrings=True,
        str_strip_whitespace=True,
    )


class EnvSettings(BaseSettings):
    DJANGO: DjangoSettings
    DATABASE: PostgresDsn

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
    )
