from telegram import Bot
import asyncio
from src.utils.config import Config

class TelegramAlertBot:
    def __init__(self):
        print("Initializing Telegram Bot...")
        self.token = Config.TELEGRAM_BOT_TOKEN
        self.bot = None
        if self.token and "your_" not in self.token:
            self.bot = Bot(token=self.token)
        else:
            print("⚠️ Telegram Token not set. Bot will run in Mock Mode.")

    async def send_alert(self, message: str, chat_id: str = None):
        """
        Send an alert message to a Telegram chat.
        """
        if self.bot and chat_id:
            try:
                await self.bot.send_message(chat_id=chat_id, text=message)
                print("✅ Telegram Alert Sent!")
            except Exception as e:
                print(f"❌ Failed to send Telegram alert: {e}")
        else:
            print(f"📢 [MOCK TELEGRAM] Sending Message:\n{message}")

if __name__ == "__main__":
    # Test the bot
    bot = TelegramAlertBot()
    asyncio.run(bot.send_alert("Test Alert from FactSeeker!"))
