"""
VERIDEX Configuration
Central location for system settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "VERIDEX"

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    USDT_POLYGON_WALLET = os.getenv("USDT_POLYGON_WALLET")

    USDC_POLYGON_WALLET = os.getenv("USDC_POLYGON_WALLET")


settings = Settings()
