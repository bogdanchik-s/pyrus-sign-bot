from __future__ import annotations

from typing import Self
from pydantic import Field
from pydantic.types import SecretStr
from pydantic_settings import BaseSettings as PydanticBaseSettings, SettingsConfigDict


class BaseSettings(PydanticBaseSettings):
    """
    Базовый класс настроек приложения
    """

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )


class KonturServiceSettings(BaseSettings):
    """
    Класс настроек сервиса Контур
    """
    
    model_config = SettingsConfigDict(env_prefix='kontur_')

    client_id: SecretStr
    client_secret: SecretStr


class Settings(BaseSettings):
    """
    Общий класс настроек приложения
    """

    kontur_service: KonturServiceSettings = Field(default_factory=KonturServiceSettings)

    @classmethod
    def load(cls) -> Self:
        return cls()


settings: Settings = Settings


def load_settings() -> None:
    global settings
    settings = settings.load()
