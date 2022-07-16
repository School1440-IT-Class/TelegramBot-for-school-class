from dotenv import load_dotenv
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(THIS_FOLDER, '.env'))

telegram_token = os.getenv("TELEGRAM_TOKEN")
owm_token = os.getenv("OWM_TOKEN")
deploy_token = os.getenv("DEPLOY_TOKEN")
