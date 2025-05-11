import customtkinter as ctk


# функция для кнопки "8" (btn1)
def press1():
    if txt_field._is_focused:  # если курсор находится в первом поле (txt_field)
        txt_field.insert(0, btn1._text)  # вставляем значение из кнопки в txt_field
    elif txt_output._is_focused:  # если курсор находится во втором поле (txt_output)
        txt_output.insert(0, btn1._text)  # вставляем значение из кнопки в txt_output


def press():
    pass


def press2():
    pass


def press3():
    pass


def press4():
    pass


def press5():
    pass


def press6():
    pass


def press7():
    pass


def press8():
    pass


def press9():
    pass


# функция для кнопки "Вычесть" (btn10)
def press10():
    k1 = int(txt_field.get())
    k2 = int(txt_output.get())
    k3 = k1 - k2
    txt_3.delete(0, 'end')  # очистка второго тектового поля
    txt_3.insert(0, str(k3))


def press11():
    pass


def press12():
    pass


# функция для кнопки "Удалить" (btn13)
def press13():
    if txt_field._is_focused:  # если курсор находится в первом поле (txt_field)
        txt_field.delete(0, 'end')  # очищаем txt_field
    elif txt_output._is_focused:  # если курсор находится во втором поле (txt_output)
        txt_output.delete(0, 'end')  # очищаем txt_output


root = ctk.CTk()
root.title('Калькулятор Дениса Александровича')
root.geometry('1000x700')
root.configure(fg_color='white')

rows, columns = 10, 10
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

start_txt = ctk.CTkLabel(master=root)
start_txt.configure(text='Калькулятор Дениса Александровича', text_color='black',
                    font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
start_txt.grid(row=0, column=2, padx=10, pady=10,columnspan=2)
# создание первого текстового поля
txt_field = ctk.CTkEntry(master=root)
txt_field.configure(justify='center', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
txt_field.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

# создание второго текстового поля
txt_output = ctk.CTkEntry(master=root)
txt_output.configure(justify='center', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
txt_output.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

txt_3 = ctk.CTkEntry(master=root)
txt_3.configure(justify='center', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
txt_3.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

btn = ctk.CTkButton(master=root)
btn.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='7',
              fg_color='black', hover_color='orange', text_color='blue', cursor='hand2', command=press)
btn.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

btn1 = ctk.CTkButton(master=root)
btn1.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='8',
              fg_color='red', hover_color='orange', text_color='blue', cursor='hand2', command=press1)
btn1.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
btn2 = ctk.CTkButton(master=root)
btn2.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='2',
              fg_color='yellow', hover_color='orange', text_color='blue', cursor='hand2', command=press2)
btn2.grid(row=4, column=2, padx=10, pady=10, sticky='nsew')
btn3 = ctk.CTkButton(master=root)
btn3.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='4',
              fg_color='green', hover_color='orange', text_color='blue', cursor='hand2', command=press3)
btn3.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')
btn4 = ctk.CTkButton(master=root)
btn4.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='5',
              fg_color='Brown', hover_color='orange', text_color='blue', cursor='hand2', command=press4)
btn4.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')
btn5 = ctk.CTkButton(master=root)
btn5.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='1',
              fg_color='Pink', hover_color='orange', text_color='blue', cursor='hand2', command=press5)
btn5.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')
btn6 = ctk.CTkButton(master=root)
btn6.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='9',
              fg_color='Purple', hover_color='orange', text_color='blue', cursor='hand2', command=press6)
btn6.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')
btn7 = ctk.CTkButton(master=root)
btn7.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='6',
              fg_color='Coral', hover_color='orange', text_color='blue', cursor='hand2', command=press7)
btn7.grid(row=3, column=3, padx=10, pady=10, sticky='nsew')

btn8 = ctk.CTkButton(master=root)
btn8.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='3',
              fg_color='lightgreen', hover_color='orange', text_color='blue', cursor='hand2', command=press8)
btn8.grid(row=4, column=3, padx=10, pady=10, sticky='nsew')
btn9 = ctk.CTkButton(master=root)
btn9.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='Сложить',
              fg_color='black', hover_color='orange', text_color='blue', cursor='hand2', command=press9)
btn9.grid(row=2, column=4, padx=10, pady=10, sticky='nsew')
btn10 = ctk.CTkButton(master=root)
btn10.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='Вычесть',
              fg_color='red', hover_color='orange', text_color='blue', cursor='hand2', command=press10)
btn10.grid(row=3, column=4, padx=10, pady=10, sticky='nsew')
btn11 = ctk.CTkButton(master=root)
btn11.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='Умножить',
              fg_color='yellow', hover_color='orange', text_color='blue', cursor='hand2', command=press11)
btn11.grid(row=4, column=4, padx=10, pady=10, sticky='nsew')
btn12 = ctk.CTkButton(master=root)
btn12.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='Разделить',
              fg_color='yellow', hover_color='orange', text_color='blue', cursor='hand2', command=press12)
btn12.grid(row=5, column=1, padx=10, pady=10, sticky='nsew')

btn13 = ctk.CTkButton(master=root)
btn13.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'), text='Удалить',
              fg_color='yellow', hover_color='orange', text_color='blue', cursor='hand2', command=press13)
btn13.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

root.mainloop()
