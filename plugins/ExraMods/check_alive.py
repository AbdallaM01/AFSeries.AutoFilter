import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("help", CMD))
async def check_alive(_, message):
    await message.reply_text("<b><a href=https://telegra.ph/%D8%AA%D8%AD%D9%85%D9%8A%D9%84-%D8%A7%D9%84%D9%85%D8%B3%D9%84%D8%B3%D9%84-%D9%88-%D8%A7%D8%B6%D8%A7%D9%81%D8%A9-%D8%A7%D9%84%D8%AA%D8%B1%D8%AC%D9%85%D8%A9-03-19>طريقة التحميل واضافة الترجمة</a></b>")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
