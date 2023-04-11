from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import load_config

config = load_config(path=".env")
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()


async def send_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)
    print(message.json(indent=4, exclude_none=True))


dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)
