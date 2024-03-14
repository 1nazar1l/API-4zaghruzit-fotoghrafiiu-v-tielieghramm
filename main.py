from telegram import Bot


bot_token = "7072799364:AAHgUr88fdlG9zVIJFFSP7X9rVM2DShY3i0"
bot = Bot(token=bot_token)
print(bot.get_me())
bot.send_message(chat_id="@dwnl_img", text="I'm sorry Dave I'm afraid I can't do that.")
