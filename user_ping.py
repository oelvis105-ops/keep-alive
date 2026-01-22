import os, asyncio
from telethon import TelegramClient

api_id   = int(os.environ["TG_API_ID"])
api_hash = os.environ["TG_API_HASH"]
bot_id   = int(os.environ["BOT_ID"])
my_id    = int(os.environ["MY_ID"])

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        await client.send_message(bot_id, "/ping")

if __name__ == "__main__":
    asyncio.run(main())