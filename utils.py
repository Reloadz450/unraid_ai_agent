import requests

def send_telegram(telegram_cfg: dict, message: str):
    """
    Send a message via Telegram Bot API.
    telegram_cfg should contain 'bot_token' and 'chat_id'.
    """
    token = telegram_cfg['bot_token']
    chat_id = telegram_cfg['chat_id']
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    requests.post(url, data=payload)
