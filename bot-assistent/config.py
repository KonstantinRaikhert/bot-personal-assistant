from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str) -> Config:
    env: Env = Env()
    env.read_env(path=path)

    config = Config(
        tg_bot=TgBot(token=env("TELEGRAM_TOKEN"), admin_ids=env("ADMIN_IDS")),
        db=DatabaseConfig(
            database=env("DATABASE"), db_host=env("DB_HOST"), db_user=env("DB_USER"), db_password=env("DB_PASSWORD")
        ),
    )
    return config
