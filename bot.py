import telebot
import openai

# المفاتيح الخاصة بك
TELEGRAM_TOKEN = "8145918766:AAFKqfwdgA-etC1APcA5oRyXudq3A5tVm0o"
OPENAI_KEY = "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"

openai.api_key = OPENAI_KEY
bot = telebot.TeleBot(TELEGRAM_TOKEN)

user_context = {}

@bot.message_handler(func=lambda message: True)
def chatgpt_reply(message):
    user_id = message.from_user.id
    user_text = message.text

    if user_id not in user_context:
        user_context[user_id] = []

    user_context[user_id].append({"role": "user", "content": user_text})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=user_context[user_id]
    )

    reply = response.choices[0].message.content
    bot.reply_to(message, reply)

    user_context[user_id].append({"role": "assistant", "content": reply})

bot.polling()
