import customtkinter as ctk


# функция, которая запускается при нажатии на кнопку
def press():
    digit = int(txt_field.get())  # получили значение из тектового поля и преобразовали его в число
    res = digit**2
    txt_output.delete(0, 'end')  # очистка второго тектового поля
    txt_output.insert(0, str(res))  # вставка результата во второе тектовое поле
    txt_field.delete(0, 'end')  # очистка первого тектового поля


# задание темы окна
ctk.set_appearance_mode('light')

# создание основного окна
root = ctk.CTk()
root.title('Моё приложение')
root.geometry('1000x700')

# отрисовка сетки основного окна
rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# создание текстовой метки
start_txt = ctk.CTkLabel(master=root)
start_txt.configure(text='Калькулятор', text_color='darkgreen',
                    font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
start_txt.grid(row=0, column=3, padx=10, pady=10)

# создание первого текстового поля
txt_field = ctk.CTkEntry(master=root)
txt_field.configure(justify='center', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
txt_field.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

# создание второго текстового поля
txt_output = ctk.CTkEntry(master=root)
txt_output.configure(justify='center', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
txt_output.grid(row=1, column=4, padx=10, pady=10, sticky='nsew')

# создание кнопки
btn = ctk.CTkButton(master=root)
btn.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='Кнопка',
              fg_color='red', hover_color='orange', text_color='blue', cursor='hand2', command=press)
btn.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')
# cursor: hand2, cross, wait

# бесконечный цикл для отображения окна
root.mainloop()
