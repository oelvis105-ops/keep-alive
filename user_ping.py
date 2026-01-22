import os, asyncio
from telethon import TelegramClient
...

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        await client.send_message(bot_id, "/ping")

if __name__ == "__main__":
    asyncio.run(main())
