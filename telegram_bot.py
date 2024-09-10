import telebot
import random
from threading import Timer

# Bot Token'inizi buraya ekleyin
BOT_TOKEN = "7009625230:AAFwimWboYn9ZdgkTKhQEOK9IrF4uQmHT0c"
bot = telebot.TeleBot(BOT_TOKEN)


# /start komutu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Merhaba! Bu bot rulet stratejileri sunar. Menü için /menu yazabilirsiniz.")


# Menü Gösterimi
@bot.message_handler(commands=['menu'])
def send_menu(message):
    bot.send_message(message.chat.id,
                     "Seçenekler:\n1. Auto Roulette\n2. Immersive Roulette\n3. Lightning Roulette\n4. Extreme Roulette\n5. Roulette Live")
    bot.register_next_step_handler(message, handle_selection)


# Menü Seçimi
def handle_selection(message):
    # Mesajı küçük harfe çevir ve boşlukları temizle
    user_input = message.text.lower().strip()

    # Sayısal veya metinsel girişe göre seçim
    if user_input == "1" or user_input == "auto roulette":
        send_auto_roulette_strategy(message.chat.id)
    elif user_input == "2" or user_input == "immersive roulette":
        bot.send_message(message.chat.id, "Henüz desteklenmeyen bir seçenek: Immersive Roulette")
    elif user_input == "3" or user_input == "lightning roulette":
        bot.send_message(message.chat.id, "Henüz desteklenmeyen bir seçenek: Lightning Roulette")
    elif user_input == "4" or user_input == "extreme roulette":
        bot.send_message(message.chat.id, "Henüz desteklenmeyen bir seçenek: Extreme Roulette")
    elif user_input == "5" or user_input == "roulette live":
        bot.send_message(message.chat.id, "Henüz desteklenmeyen bir seçenek: Roulette Live")
    else:
        bot.send_message(message.chat.id, "Geçersiz seçim. Lütfen geçerli bir seçenek girin.")


# Auto Roulette Strateji Gönderimi
def send_auto_roulette_strategy(chat_id):
    def generate_strategy():
        numbers = random.sample(range(0, 37), 3)
        strategy_message = f"Sıradaki Spin Oynanacak Sayılar: {numbers[0]}-{numbers[1]}-{numbers[2]} \n(3 Komşulu olarak oyna)"
        bot.send_message(chat_id, strategy_message)

    # Her dakika strateji gönderimi için Timer kullanımı
    def start_timer():
        generate_strategy()
        Timer(60, start_timer).start()

    start_timer()


# Botu Başlat
bot.polling()
