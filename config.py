from dotenv import load_dotenv
import os

load_dotenv()

telegram_token = os.getenv("TELEGRAM_TOKEN")
owm_token = os.getenv("OWM_TOKEN")
