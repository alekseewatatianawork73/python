import customtkinter as ctk


def press1():
    s = entr.get()
    s = s.upper()
    entr.delete(0, 'end')
    entr.insert(0, s)


def press2():
    s = entr.get()
    s = s.lower()
    entr.delete(0, 'end')
    entr.insert(0, s)


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
btn.configure(text='Преобразовать в верхний регистр', command=press1, font=ctk.CTkFont(family='Arial', size=15, weight='bold', slant='italic'))
btn.grid(row=3, column=3, padx=20, pady=20, sticky='ew')

btn = ctk.CTkButton(master=root)
btn.configure(text='Преобразовать в нижний регистр', command=press2, font=ctk.CTkFont(family='Arial', size=15, weight='bold', slant='italic'))
btn.grid(row=4, column=3, padx=20, pady=20, sticky='ew')

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Работа со строками', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky='ew')

entr = ctk.CTkEntry(master=root)
entr.configure(justify='center', font=ctk.CTkFont(family='Arial', size=15), state='normal')
entr.grid(row=1, column=3, padx=20, pady=20, sticky='nsew')

root.mainloop()




