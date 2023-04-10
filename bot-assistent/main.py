from aiogram import Bot, Dispatcher
from get_env import TELEGRAM_TOKEN

bot: Bot = Bot(token=TELEGRAM_TOKEN)
dp: Dispatcher = Dispatcher()


def main():
    pass


if __name__ == "__main__":
    dp.run_polling(bot)
