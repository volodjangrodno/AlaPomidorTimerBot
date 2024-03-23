Под каждой из функций<br/> 
***def send_reminders***<br/>
Замените время на подходящее вам (обязательно в формате HH:MM)<br/>
Это будет время различных вариантов напоминаний в Телеграм-чате.<br/>
**Напоминания о начале работы после долгого перерыва:**
***def send_reminders1***<br/>
- work_time1 = "12:00"
- work_time5 = "16:00"
- work_time9 = "20:00"

**Напоминания о начале короткого перерыва:**
***def send_reminders2, def send_reminders5, def send_reminders7***<br/>
- short_repas1 = "12:25"
- short_repas2 = "12:55"
- short_repas3 = "13:25"


- short_repas5 = "16:25"
- short_repas6 = "16:55"
- short_repas7 = "17:25"


- short_repas9 = "20:25"
- short_repas10 = "20:55"
- short_repas11 = "21:25"

**Напоминания о начале работы после короткоого перерыва:**
***def send_reminders3, def send_reminders6, def send_reminders8***<br/>
- work_time2 = "12:30"
- work_time3 = "13:00"
- work_time4 = "13:30"


- work_time6 = "16:30"
- work_time7 = "17:00"
- work_time8 = "17:30"


- work_time10 = "20:30"
- work_time11 = "21:00"
- work_time12 = "21:30"

**Напоминания о начале долгого перерыва:**
***def send_reminders4***<br/>
- long_repas1 = "14:00"
- long_repas2 = "18:00"

**Напоминания о конце рабочего дня:**
***def send_reminders9***<br/>
 - end_work = "22:00"

**При желании вы можете изменить сам текст напоминаний** 
в ковычках внутри командных строк <br/>
например:
bot.send_message(chat_id, "Хватит спать! Работы ВАГОН!")