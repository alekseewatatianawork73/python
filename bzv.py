import random
import customtkinter as ctk

winplr = 0
winbot = 0


def gotov():
    global winplr
    global winbot
    bzvplr = txt_field.get() # б и з = з, б и в = б, з и в = в
    bzvlst = ['бутылка', 'закуска', 'вилка']
    bzvbot = random.choice(bzvlst)
    win = 1

    #print(f'Ваш ответ: {bzvplr}')
    #print(f'Ответ бота: {bzvbot}')

    if bzvplr == 'бутылка' and bzvbot == 'закуска':
        win = 0
        winbot = winbot + 1
    elif bzvplr == 'бутылка' and bzvbot == 'вилка':
        win = 1
        winplr = winplr + 1
    elif bzvplr == 'закуска' and bzvbot == 'бутылка':
        win = 1
        winplr = winplr + 1
    elif bzvplr == 'закуска' and bzvbot == 'вилка':
        win = 0
        winbot = winbot + 1
    elif bzvplr == 'вилка' and bzvbot == 'закуска':
        win = 1
        winplr = winplr + 1
    elif bzvplr == 'вилка' and bzvbot == 'бутылка':
        win = 0
        winbot = winbot + 1
    elif bzvplr == 'вилка' and bzvbot == 'вилка':
        win = 2
    elif bzvplr == 'закуска' and bzvbot == 'закуска':
        win = 2
    elif bzvplr == 'бутылка' and bzvbot == 'бутылка':
        win = 2
    else:
        win = 3

    if win == 0:
        txt_res.configure(state='normal')
        txt_res.delete(0, 'end')
        txt_res.insert(0, format(str(f'Ответ бота: {bzvbot}. Вы проиграли!')))
        txt_res.configure(state='disabled')
    elif win == 1:
        txt_res.configure(state='normal')
        txt_res.delete(0, 'end')
        txt_res.insert(0, format(str(f'Ответ бота: {bzvbot}. Вы выиграли!')))
        txt_res.configure(state='disabled')
    elif win == 2:
        txt_res.configure(state='normal')
        txt_res.delete(0, 'end')
        txt_res.insert(0, format(str(f'Ответ бота: {bzvbot}. Ничья!')))
        txt_res.configure(state='disabled')
    elif win == 3:
        txt_res.configure(state='normal')
        txt_res.delete(0, 'end')
        txt_res.insert(0, format(str(f'Некорректный ответ!')))
        txt_res.configure(state='disabled')

    score_txt.configure(text=f'Игрок | {winplr}:{winbot} | Бот')


# python setup.py build <- преобразование .py в .exe


th = 'dark'
ctk.set_appearance_mode(th)

root = ctk.CTk()
root.title('БЗВ')
root.geometry('1200x700')

rows, columns = 7, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

start_txt = ctk.CTkLabel(master=root)
start_txt.configure(text='Добро пожаловать в игру "Бутылка-закуска-вилка"! Знаем, название странное, но игра имбовая! Буду рад, если ты зайдёшь на мой сайт - http://simakov.rf.gd', text_color='white',
                    font=ctk.CTkFont(family='Comic Sans MS', size=15, weight='bold'))
start_txt.grid(row=0, column=1, padx=10, pady=10)

instruktsiya_txt = ctk.CTkLabel(master=root)
instruktsiya_txt.configure(text='Иструкция:\n1) Вы пишете либо "бутылка", либо "закуска", либо "вилка" (на ваш выбор).\n2) Бот выбирает рандом.\n3) Результаты!\n--> Кто кого бьёт <--\nБутылка гнёт вилку, закуска пачкает бутылку, а вилка портит закуску.', text_color='yellow',
                    font=ctk.CTkFont(family='Comic Sans MS', size=15, weight='bold'))
instruktsiya_txt.grid(row=1, column=1, padx=10, pady=10)

score_txt = ctk.CTkLabel(master=root)
score_txt.configure(text=f'Игрок | {winplr}:{winbot} | Бот', text_color='yellow',
                    font=ctk.CTkFont(family='Comic Sans MS', size=20, weight='bold'))
score_txt.grid(row=2, column=1, padx=10, pady=10)

txt_field = ctk.CTkEntry(master=root)
txt_field.configure(justify='center', font=ctk.CTkFont(family='Comic Sans MS', size=20, weight='bold'))
txt_field.grid(row=3, column=1, padx=400, pady=10, sticky='nsew')

btngotov = ctk.CTkButton(master=root)
btngotov.configure(font=ctk.CTkFont(family='Comic Sans MS', size=15, weight='bold'), text='Узнать',
              fg_color='yellow', hover_color='orange', text_color='black', cursor='hand2', command=gotov)
btngotov.grid(row=4, column=1, padx=400, pady=10, sticky='nsew')

txt_res = ctk.CTkEntry(master=root)
txt_res.configure(justify='center', state='disabled', font=ctk.CTkFont(family='Comic Sans MS', size=20, weight='bold'))
txt_res.grid(row=5, column=1, padx=400, pady=10, sticky='nsew')

root.mainloop()
