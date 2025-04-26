import customtkinter as ctk


def light():
    ctk.set_appearance_mode("light")
    rad2.deselect()  # делаем радиокнопку 2 неактивной


def dark():
    rad1.deselect()  # делаем радиокнопку 1 неактивной
    ctk.set_appearance_mode("dark")


def press1():
    # создаём всплывающее окно
    window = ctk.CTkToplevel(master=root)
    window.title('Меню')
    window.geometry('700x300')


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x700")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# создаём первую радиокнопку
rad1 = ctk.CTkRadioButton(master=root)
rad1.configure(text='Светлый фон', font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=light)
rad1.grid(row=1, column=2, padx=20, pady=20, sticky="ew")

# создаём вторую радиокнопку
rad2 = ctk.CTkRadioButton(master=root)
rad2.configure(text='Тёмный фон', font=ctk.CTkFont(family='Arial', size=20, weight='bold', slant='italic'), command=dark)
rad2.grid(row=1, column=4, padx=20, pady=20, sticky="ew")

btn = ctk.CTkButton(master=root)
btn.configure(corner_radius=100, text="Открыть меню", font=ctk.CTkFont(family='Arial', size=20, weight='bold'), command=press1)
# corner_radius - делает кнопку круглой, чем больше значение, тем более закруглены края
btn.grid(row=3, column=3, padx=10, pady=10, sticky="ns")

root.mainloop()
