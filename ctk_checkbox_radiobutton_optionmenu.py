import customtkinter as ctk
count = 3
count1 = 3


def press1():
    global count
    t = ctk.CTkCheckBox(master=root)
    t.configure(text=f'Вариант {count - 2}', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    t.grid(row=count, column=2, padx=10, pady=10)
    count += 1


def press2():
    global count1
    r = ctk.CTkRadioButton(master=root)
    r.configure(text=f'Кнопка {count1 - 2}', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
    r.grid(row=count1, column=4, padx=10, pady=10)
    count1 += 1


# функция: что будет происходить при выборе значения в меню
def om(ch):
    if ch == 'Тёмный фон':
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x500")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)


menu = ctk.CTkOptionMenu(master=root)
menu.configure(command=om, values=['Тёмный фон', 'Светлый фон'], font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
menu.set('Выберите тему фона')
menu.grid(row=0, column=3, padx=20, pady=20)

entr = ctk.CTkEntry(master=root)
entr.configure(justify="center", state="normal", font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
entr.grid(row=1, column=3, padx=20, pady=20, sticky="nsew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Checkbox", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press1)
btn1.grid(row=2, column=2, padx=20, pady=20, sticky="ew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Radiobutton", font=ctk.CTkFont(family='Arial', size=15, weight='bold'), command=press2)
btn2.grid(row=2, column=4, padx=20, pady=20, sticky="ew")

root.mainloop()
