import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Pomodoro Timer")

# Функции таймера
def start_timer():
    global timer_active
    if not timer_active:
        timer_active = True
        update_timer()

def stop_timer():
    global timer_active
    timer_active = False

def reset_timer():
    global timer_active, current_time, cycles
    timer_active = False
    current_time = work_min.get() * 60
    cycles.set(0)
    update_timer_display(current_time)
    cycles_label.config(text=f"Циклы: {cycles.get()}")

# Функция обновления таймера
def update_timer():
    global current_time
    if timer_active:
        if current_time > 0:
            current_time -= 1
            update_timer_display(current_time)
            root.after(1000, update_timer)
        else:
            finish_cycle()

# Функция завершения цикла
def finish_cycle():
    global current_mode, current_time, cycles
    if current_mode == "work":
        cycles.set(cycles.get() + 1)
        if cycles.get() % 4 == 0:
            current_mode = "long_break"
            current_time = long_break_min.get() * 60
        else:
            current_mode = "short_break"
            current_time = short_break_min.get() * 60

    elif current_mode in ["short_break", "long_break"]:
        current_mode = "work"
        current_time = work_min.get() * 60

    update_timer_display(current_time)
    cycles_label.config(text=f"Циклы: {cycles.get()}")
    if timer_active:
        root.after(1000, update_timer)

def update_timer_display(time):
    minutes = time // 60
    seconds = time % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

work_min = tk.IntVar(value=2) # Продолжительность работы
short_break_min = tk.IntVar(value=1) # Продолжительность короткого перерыва
long_break_min = tk.IntVar(value=3) # Продолжительность долгого перерыва
cycles = tk.IntVar(value=0) # Количество завершённых помодоро-циклов

# Названия полей ввода времени
work_label = tk.Label(root, text="Работа")
short_break_min_label = tk.Label(root, text="Короткий перерыв")
long_break_min_label = tk.Label(root, text="Долгий перерыв")

# Поля для ввода времени
work_entry = tk.Entry(root, textvariable=work_min)
short_break_entry = tk.Entry(root, textvariable=short_break_min)
long_break_entry = tk.Entry(root, textvariable=long_break_min)

# Кнопки управления
start_button = tk.Button(root, text="Старт", command=start_timer)
stop_button = tk.Button(root, text="Стоп", command=stop_timer)
reset_button = tk.Button(root, text="Сброс", command=reset_timer)

# Отображение таймера и циклов
timer_label = tk.Label(root, text="00:00")  # Таймер
cycles_label = tk.Label(root, text="0")  # Циклы

current_mode = "work"  # Текущий режим работы (работа, короткий перерыв, долгий перерыв)
current_time = work_min.get() * 60  # Текущее время работы
timer_active = False  # Состояние таймера (на активен)

# Размещение названий полей
work_label.grid(row=0, column=0)
short_break_min_label.grid(row=2, column=0)
long_break_min_label.grid(row=4, column=0)

# Размещение элементов на экране
work_entry.grid(row=1, column=0)
short_break_entry.grid(row=3, column=0)
long_break_entry.grid(row=5, column=0)

start_button.grid(row=0, column=1)
stop_button.grid(row=0, column=2)
reset_button.grid(row=0, column=3)

timer_label.grid(row=1, column=1)
cycles_label.grid(row=1, column=3)



root.mainloop()