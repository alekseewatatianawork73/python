import customtkinter as ctk


def press():
    entr.configure(state="normal")
    entr.insert(0, 'Кнопка нажата.')
    entr.configure(state="disabled")


def delet():
    entr.configure(state="normal")
    entr.delete(0, 'end')
    entr.configure(state="disabled")


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
btn.configure(text='Ввести текст', command=press, font=ctk.CTkFont(family='Arial', size=15, weight='bold', slant='italic'))
btn.grid(row=3, column=3, padx=20, pady=20, sticky='ew')

btn = ctk.CTkButton(master=root)
btn.configure(text='Удалить текст', command=delet, font=ctk.CTkFont(family='Arial', size=15, weight='bold', slant='italic'))
btn.grid(row=4, column=3, padx=20, pady=20, sticky='ew')

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Приложение с кнопкой', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky='ew')

entr = ctk.CTkEntry(master=root)
entr.configure(justify='left', font=ctk.CTkFont(family='Arial', size=15), state='disabled')
entr.grid(row=1, column=3, padx=20, pady=20, sticky='nsew')

root.mainloop()
