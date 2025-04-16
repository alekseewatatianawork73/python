import customtkinter as ctk


# функция, которая выполняется, когда мы делаем выбор в выпадающем списке
def press_cmb(choice):
    pass


# функция для кнопки
def press_btn():
    d = int(entr1.get())  # получаем значение из поля для ввода entr1
    res = 0  # переменная для результата
    # проверяем, какое значение выбрано в выпадающем списке
    if cmb.get() == 'Возведение в квадрат':
        res = d * d
    elif cmb.get() == 'Возведение в куб':
        res = d**3
    else:
        res = d**0.5
    entr2.configure(state='normal')  # переводим поле entr2 в нормальное состояние
    entr2.delete(0, 'end')  # удаляем предыдущее значение
    entr2.insert(0, str(res))  # вставляем полученный результат
    entr2.configure(state='disabled')  # снова делаем поле entr2 неизменяемым


root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x500")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Операции над числами', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

# создаём выпадающий список
cmb = ctk.CTkComboBox(master=root)
cmb.configure(command=press_cmb, justify='center', values=['Возведение в квадрат', 'Возведение в куб', 'Извлечение корня'], font=ctk.CTkFont(family='Arial', size=15))
# values - значения, которые есть в выпадающем списке
cmb.set('Возведение в квадрат')  # значение, которое отображается при запуске
cmb.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

entr1 = ctk.CTkEntry(master=root)
entr1.configure(justify="center", state="normal")
entr1.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

entr2 = ctk.CTkEntry(master=root)
entr2.configure(justify="center", state="disabled")
entr2.grid(row=2, column=4, padx=20, pady=20, sticky="nsew")

btn = ctk.CTkButton(master=root)
btn.configure(text="Результат", font=ctk.CTkFont(family='Arial', size=15, weight='bold'),
              command=press_btn)
btn.grid(row=3, column=3, padx=20, pady=20, sticky="ew")

root.mainloop()
