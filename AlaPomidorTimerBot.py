import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("Введите сюда токен своего бота")

@bot.message_handler(commands=["start"])

def start_message(message):
    bot.reply_to(message, "Привет! Я чат бот, который будет тебе напоминать об интервалах работы и перерывах между ними!")

    reminder_thread1 = threading.Thread(target=send_reminders1, args=(message.chat.id,))
    reminder_thread1.start()

    reminder_thread2 = threading.Thread(target=send_reminders2, args=(message.chat.id,))
    reminder_thread2.start()

    reminder_thread3 = threading.Thread(target=send_reminders3, args=(message.chat.id,))
    reminder_thread3.start()

    reminder_thread4 = threading.Thread(target=send_reminders4, args=(message.chat.id,))
    reminder_thread4.start()

    reminder_thread5 = threading.Thread(target=send_reminders5, args=(message.chat.id,))
    reminder_thread5.start()

    reminder_thread6 = threading.Thread(target=send_reminders6, args=(message.chat.id,))
    reminder_thread6.start()

    reminder_thread7 = threading.Thread(target=send_reminders7, args=(message.chat.id,))
    reminder_thread7.start()

    reminder_thread8 = threading.Thread(target=send_reminders8, args=(message.chat.id,))
    reminder_thread8.start()

    reminder_thread9 = threading.Thread(target=send_reminders9, args=(message.chat.id,))
    reminder_thread9.start()

@bot.message_handler(commands=["fact"])

def fact_message(message):
    list = [
        "Улучшение концентрации: Чередование коротких периодов работы с перерывами на отдых помогает поддерживать высокую концентрацию и предотвращает умственную усталость, позволяя мозгу восстанавливаться и поддерживать эффективность на протяжении всего дня.",
        "Способствует творчеству и решению задач: Регулярные перерывы в работе стимулируют креативность и улучшают способность к решению проблем, так как отдых дает возможность мозгу отходить от линейного мышления и подходить к вопросам с разных сторон.",
        "Повышение продуктивности и избегание перегрузок: Периодические перерывы помогают предотвратить переутомление и стресс, тем самым сокращая риск выгорания. Это способствует поддержанию высокой уровня продуктивности и лучшему общему психическому здоровью."]

    random_fact = random.choice(list)
    bot.reply_to(message, f"Лови факт о необходимости чередования работы и отдыха {random_fact}")

def send_reminders1(chat_id):

    work_time1 = "12:00"
    work_time5 = "16:00"
    work_time9 = "20:00"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == work_time1 or now == work_time5 or now == work_time9:
            bot.send_message(chat_id, "Хватит спать! Работы ВАГОН!")
            time.sleep(61)
        time.sleep(1)

def send_reminders2(chat_id):

    short_repas1 = "12:25"
    short_repas2 = "12:55"
    short_repas3 = "13:25"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == short_repas1 or now == short_repas2 or now == short_repas3:
            bot.send_message(chat_id, "Отдохни 5 мин!")
            time.sleep(61)
        time.sleep(1)

def send_reminders3(chat_id):

    work_time2 = "12:30"
    work_time3 = "13:00"
    work_time4 = "13:30"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == work_time2 or now == work_time3 or now == work_time4:
            bot.send_message(chat_id, "Отдохнул 5 мин? За работу!")
            time.sleep(61)
        time.sleep(1)

def send_reminders4(chat_id):

    long_repas1 = "14:00"
    long_repas2 = "18:00"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == long_repas1 or now == long_repas2:
            bot.send_message(chat_id, "Харэ работать! Перекуси, покемарь чуток")
            time.sleep(61)
        time.sleep(1)

def send_reminders5(chat_id):

    short_repas5 = "16:25"
    short_repas6 = "16:55"
    short_repas7 = "17:25"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == short_repas5 or now == short_repas6 or now == short_repas7:
            bot.send_message(chat_id, "Отдохни 5 мин! Но не расслабляйся!")
            time.sleep(61)
        time.sleep(1)

def send_reminders6(chat_id):

    work_time6 = "16:30"
    work_time7 = "17:00"
    work_time8 = "17:30"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == work_time6 or now == work_time7 or now == work_time8:
            bot.send_message(chat_id, "Отдохнул 5 мин? За работу - Солнце ещё высоко!")
            time.sleep(61)
        time.sleep(1)

def send_reminders7(chat_id):

    short_repas9 = "20:25"
    short_repas10 = "20:55"
    short_repas11 = "21:25"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == short_repas9 or now == short_repas10 or now == short_repas11:
            bot.send_message(chat_id, "Отдохни 5 мин! Конец рабочего дня уже близок!")
            time.sleep(61)
        time.sleep(1)

def send_reminders8(chat_id):

    work_time10 = "20:30"
    work_time11 = "21:00"
    work_time12 = "21:30"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == work_time10 or now == work_time11 or now == work_time12:
            bot.send_message(chat_id, "Отдохнул 5 мин? За работу - Ты на финишной прямой!")
            time.sleep(61)
        time.sleep(1)

def send_reminders9(chat_id):

    end_work = "22:00"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == end_work:
            bot.send_message(chat_id, "Ну вот и всё - Ты победил сегодня! А завтра нас с тобой ждут ВЕЛИКИЕ дела!")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)