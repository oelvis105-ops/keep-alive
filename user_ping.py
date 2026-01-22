import os, asyncio
from telethon import TelegramClient

api_id   = int(os.environ["32454773"])
api_hash = os.environ["f9789ae28af20dce11468e4f028dbe6b"]
bot_id   = int(os.environ["8580432369"])
my_id    = int(os.environ["1836471542"])

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        await client.send_message(bot_id, "/ping")

if __name__ == "__main__":
    asyncio.run(main())
