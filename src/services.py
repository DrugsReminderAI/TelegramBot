import logging
import aiohttp
from .config import BACKEND_URL

async def send_to_backend(message):
    logging.info(f"[MOCK] would send to backend: {message}")
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(BACKEND_URL, json=message) as resp:
                if resp.status != 200:
                    logging.warning(f"Ошибка отправки: {resp.status}")
                    return None
                return await resp.json()  # 👈 вернём ответ от бэка
        except Exception as e:
            logging.error(f"Ошибка связи с backend: {e}")
            return None