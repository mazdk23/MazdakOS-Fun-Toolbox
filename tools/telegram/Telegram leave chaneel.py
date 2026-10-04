from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest

api_id = 12345678
api_hash = "YOUR_API_HASH"

client = TelegramClient("session", api_id, api_hash)

async def main():
    channels = []

    async for dialog in client.iter_dialogs():
        if dialog.is_channel and not dialog.is_group:
            channels.append(dialog)

    print(f"\nتعداد کانال‌ها: {len(channels)}\n")

    for i, channel in enumerate(channels, 1):
        print(f"{i}. {channel.name}")

    print("\nبرای خروج از همه کانال‌ها، ALL را وارد کن.")
    choice = input("انتخاب: ")

    if choice.upper() == "ALL":
        for channel in channels:
            print(f"Leaving: {channel.name}")
            await client(LeaveChannelRequest(channel.entity))

        print("\nتمام کانال‌ها ترک شدند.")

with client:
    client.loop.run_until_complete(main())