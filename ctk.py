import customtkinter as ctk


def press():
    print('Кнопка нажата.')


ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.geometry('1000x500')
root.title('Моё приложение')

r, c = 7, 7
for i in range(r):
    root.rowconfigure(i, weight=1)
for i in range(c):
    root.columnconfigure(i, weight=1)

btn = ctk.CTkButton(master=root)
btn.configure(text='Получить результат', command=press, font=ctk.CTkFont(family='Arial', size=15, weight='bold', slant='italic'))
btn.grid(row=3, column=3, padx=20, pady=20, sticky='ew')

root.mainloop()
