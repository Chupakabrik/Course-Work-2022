# ------------------------------------ << БИБЛИОТЕКИ >> ------------------------------------- #
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from db import *


# ------------------------------------------------------------------------------------------- #


# ------------------------------------ << РАБОТА С БД >> ------------------------------------ #

# ------------------------------------------------------------------------- #

class Document_types():

    def __init__(self):
        self.db = db   # экземпляр класса DB
        self.variable = []
        self.selected_item = 0
        self.viewRecords()
        #self.funcs()

    # ------------------------ ФУНКЦИИ БД (Виды документов) ----------------------- #
    def viewRecords(self):
        ''' Вывод данных '''
        self.db.cur.execute(
            '''SELECT * FROM Document_types''')
        self.variable.clear()   # очищаем прошлые данные (чтобы не дублировались)
        [self.variable.append(row) for row in self.db.cur.fetchall()]   # записываем новый результат

    # ------------------------- TKINTER (Виды документов) ------------------------- #

    def tableDocument_types(self):
        ''' Создание таблицу с помощью ttk.Treeview() '''
        # Задаем расположение таблицы
        frame = tk.Frame(root, width=100, height=100)
        frame.place(x=10, y=140)

       # Создаем заголовоки для таблицы
        headers = ['ID', 'Код вида', 'Нaзвание']
        self.table = ttk.Treeview(frame, columns=headers, height=15, show='headings')

        self.table.column('ID', width=50, anchor='center') 
        self.table.column('Код вида', width=200, anchor='center') 
        self.table.column('Нaзвание', width=550, anchor='center')
        
        for header in headers:  # заполняем заголовоки
            self.table.heading(header, text=header)
            
        for i in self.variable: # заполняем значения
            self.table.insert('', tk.END, values=i)

        # Создаем скролл для таблицы
        scroll = ttk.Scrollbar(frame, command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH)
 
    def editDocument_types(self):
        ''' Редактирование таблицы '''
        def closeFunc():
            z.destroy() # закрываем окно

        # Создаем новое окно
        z = Toplevel()
        z.geometry('225x200')
        z.title('Edit')
        z.resizable(False, False)

        # Получаем данные строки по клику
        selected_item = self.table.selection()[0]
        values = self.table.item(selected_item, option='values')

        # Заносим данные строки в переменные
        id = values[0]
        view_code = values[1]
        name = values[2]

        # Создаем метки и их расположение
        view_code_label = Label(z, text='Код вида').place(x=10, y=10, width=70, height=30)
        name_label = Label(z, text='Нaзвание').place(x=10, y=60, width=70, height=30)

        # Переменные для ввода значений
        view_code_1 = StringVar()
        name_2 = StringVar()

        # Строки для ввода значений
        view_code_entry = Entry(z, width=50, textvariable=view_code_1)
        name_entry = Entry(z, width=50, textvariable=name_2)

        # Записываем значения из строк ввода
        view_code_entry.insert(0, str(view_code))
        name_entry.insert(0, str(name))

        # Задаем расположение строк ввода
        view_code_entry.place(x=100, y=10, width=100, height=30)
        name_entry.place(x=100, y=60, width=100, height=30)

        # Создаем кнопку "Редактировать"
        edit_button = Button(z, text='Редактировать', command=lambda:
                             (self.db.updateRecord1(view_code_1.get(), name_2.get(), id), self.viewRecords(), self.tableDocument_types()))
        edit_button.place(x=10, y=160, width=100, height=30)

        # Создаем кнопку "Закрыть"
        close_button = Button(z, text='Закрыть', command=closeFunc)
        close_button.place(x=115, y=160, width=100, height=30)
              
    def idDelete(self):
        ''' Удаление строки по id из БД '''
        self.selected_item = self.table.selection()[0]  # получаем строку
        values = self.table.item(self.selected_item, option='values')   # получаем значения строки
        delete_id = values[0]   # получаем id строки
        self.db.deleteRecords1(delete_id)   # удаляем строку по полученному id
        
    def lineDelete(self):
        ''' Удаление выбранной строки из таблицы tkinter '''
        self.table.delete(self.selected_item)   # удаляем полученную строку


# ------------------------------  Отделы  ------------------------------ #
# ----------------------------------------------------------------------- #
 
class Departments():

    def __init__(self):
        self.db = db   # экземпляр класса DB
        self.variable = []
        self.selected_item = 0
        self.viewRecords()

    # ------------------------- ФУНКЦИИ БД (Отделы) ------------------------ #

    def viewRecords(self):
        ''' Вывод данных '''
        self.db.cur.execute(
            '''SELECT * FROM Departments''')
        self.variable.clear()   # очищаем прошлые данные (чтобы не дублировались)
        [self.variable.append(row) for row in self.db.cur.fetchall()]   # записываем новый результат

    # -------------------------- TKINTER (Отделы) -------------------------- #

    def tableDepartments(self):
        ''' Создание таблицу с помощью ttk.Treeview() '''
        # Задаем расположение таблицы
        frame = tk.Frame(root, width=100, height=100)
        frame.place(x=10, y=140)

       # Создаем заголовоки для таблицы
        headers = ['ID', 'Код_отдела', 'Название']
        self.table = ttk.Treeview(frame, columns=headers, height=15, show='headings')
        
        self.table.column('ID', width=50, anchor='center')
        self.table.column('Код_отдела', width=200, anchor='center') 
        self.table.column('Название', width=550, anchor='center')
        
        
        for header in headers:  # заполняем заголовоки
            self.table.heading(header, text=header)
            
        for i in self.variable: # заполняем значения
            self.table.insert('', tk.END, values=i)

        # Создаем скролл для таблицы
        scroll = ttk.Scrollbar(frame, command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH)
  
    def editDepartments(self):
        ''' Редактирование таблицы '''
        def closeFunc():
            z.destroy() # закрываем окно

        # Создаем новое окно
        z = Toplevel()
        z.geometry('270x230')
        z.title('Edit')
        z.resizable(False, False)

        # Получаем данные строки по клику
        selected_item = self.table.selection()[0]
        values = self.table.item(selected_item, option='values')

        # Заносим данные строки в переменные
        id = values[0]
        department_code = values[1]
        title = values[2]


        # Создаем метки и их расположение
        department_code_label = Label(z, text='Код_отдела').place(x=10, y=10, width=80, height=30)
        title_label = Label(z, text='Название').place(x=10, y=60, width=80, height=30)
        

        # Переменные для ввода значений
        department_code_1 = StringVar()
        title_3 = StringVar()


        # Строки для ввода значений
        department_code_entry = Entry(z, width=50, textvariable=department_code_1)
        title_entry = Entry(z, width=50, textvariable=title_3)


        # Записываем значения из строк ввода
        department_code_entry.insert(0, str(department_code))
        title_entry.insert(0, str(title))


        # Задаем расположение строк ввода
        department_code_entry.place(x=130, y=10, width=130, height=30)
        title_entry.place(x=130, y=60, width=130, height=30)

        # Создаем кнопку "Редактировать"
        edit_button = Button(z, text='Редактировать', command=lambda:
                             (self.db.updateRecord2(department_code_1.get(), title_3.get(), id), self.viewRecords(), self.tableDepartments()))
        edit_button.place(x=10, y=190, width=100, height=30)

        # Создаем кнопку "Закрыть"
        close_button = Button(z, text='Закрыть', command=closeFunc)
        close_button.place(x=115, y=190, width=100, height=30)
        
    def idDelete(self):
        ''' Удаление строки по id из БД '''
        self.selected_item = self.table.selection()[0]  # получаем строку
        values = self.table.item(self.selected_item, option='values')   # получаем значения строки
        delete_id = values[0]   # получаем id строки
        self.db.deleteRecords2(delete_id)   # удаляем строку по полученному id
        
    def lineDelete(self):
        ''' Удаление выбранной строки из таблицы tkinter '''
        self.table.delete(self.selected_item)   # удаляем полученную строку


# ------------------------------ Документы ------------------------------ #
# -------------------------------------------------------------------- #

class Documents():

    def __init__(self):
        self.db = db   # экземпляр класса DB
        self.variable = []
        self.selected_item = 0
        self.viewRecords()

    # -------------------------- ФУНКЦИИ БД (Документы) -------------------------- #
    def viewRecords(self):
        ''' Вывод данных '''
        self.db.cur.execute(
            '''SELECT * FROM Documents''')
        self.variable.clear()   # очищаем прошлые данные (чтобы не дублировались)
        [self.variable.append(row) for row in self.db.cur.fetchall()]   # записываем новый результат

    # ---------------------------- TKINTER (Документы) --------------------------- #

    def tableDocuments(self):
        ''' Создание таблицу с помощью ttk.Treeview() '''
        # Задаем расположение таблицы
        frame = tk.Frame(root, width=100, height=100)
        frame.place(x=10, y=140)

        # Создаем заголовоки для таблицы
        headers = ['ID', 'Код документа', 'Название', 'Номер', 'Код_вида', 'Код_отдела-отправителя', 'Код_отдела-получателя', 'Дата регистрации']
        self.table = ttk.Treeview(frame, columns=headers, height=15, show='headings')
        
        self.table.column('ID', width=50, anchor='center')
        self.table.column('Код документа', width=100, anchor='center') 
        self.table.column('Название', width=100, anchor='center')
        self.table.column('Номер', width=50, anchor='center')
        self.table.column('Код_вида', width=100, anchor='center')
        self.table.column('Код_отдела-отправителя', width=135, anchor='center')
        self.table.column('Код_отдела-получателя', width=135, anchor='center')
        self.table.column('Дата регистрации', width=130, anchor='center')

        
        for header in headers:  # заполняем заголовоки
            self.table.heading(header, text=header)
            
        for i in self.variable: # заполняем значения
            self.table.insert('', tk.END, values=i)

        # Создаем скролл для таблицы
        scroll = ttk.Scrollbar(frame, command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH)
 
    def editDocuments(self):
        ''' Редактирование таблицы '''
        def closeFunc():
            z.destroy() # закрываем окно
            

        # Создаем новое окно
        z = Toplevel()
        z.geometry('260x350')
        z.title('Edit')
        z.resizable(False, False)

        # Получаем данные строки по клику
        selected_item = self.table.selection()[0]
        values = self.table.item(selected_item, option='values')

        # Заносим данные строки в переменные
        id = values[0]
        Document_code = values[1]
        Appellation = values[2]
        Number = values[3]
        View_code = values[4]
        Documentcodes = values[5]
        Documentcoder = values[6]
        Reg_date = values[7]

        # Создаем метки и их расположение
        Document_code_label = Label(z, text='Код документа').place(x=20, y=10, width=100, height=30)
        Appellation_label = Label(z, text='Название').place(x=20, y=60, width=100, height=30)
        Number_label = Label(z, text='Номер').place(x=20, y=100, width=100, height=30)
        View_code_label = Label(z, text='Код_вида').place(x=20, y=140, width=100, height=30)
        Documentcodes_label = Label(z, text='Код_отдела-отправителя').place(x=20, y=180, width=135, height=30)
        Documentcoder_label = Label(z, text='Код_отдела-получателя').place(x=20, y=220, width=135, height=30)
        Reg_date_label = Label(z, text='Дата регистрации').place(x=20, y=260, width=120, height=30)

        # Переменные для ввода значений
        Document_code_1 = StringVar()
        Appellation_2 = StringVar()
        Number_3 = StringVar()
        View_code_4 = StringVar()
        Documentcodes_5 = StringVar()
        Documentcoder_6 = StringVar()
        Reg_date_7 = StringVar()

        # Строки для ввода значений
        Document_code_entry = Entry(z, width=50, textvariable=Document_code_1)
        Appellation_entry = Entry(z, width=50, textvariable=Appellation_2)
        Number_entry = Entry(z, width=50, textvariable=Number_3)
        View_code_entry = Entry(z, width=50, textvariable=View_code_4)
        Documentcodes = Entry(z, width=50, textvariable=Documentcodes_5)
        Documentcoder = Entry(z, width=50, textvariable=Documentcoder_6)
        Reg_date = Entry(z, width=50, textvariable=Reg_date_7)

        # Записываем значения из строк ввода
        Document_code_entry.insert(0, str(Document_code))
        Appellation_entry.insert(0, str(Appellation))
        Number_entry.insert(0, str(Number))
        View_code_entry.insert(0, str(View_code))
        #Documentcodes_entry.insert(0, str(Documentcodes))
        #Documentcoder_entry.insert(0, str(Documentcoder))
        #Reg_date_entry.insert(0, str(Reg_date))

        # Задаем расположение строк ввода
        Document_code_entry.place(x=110, y=10, width=120, height=30)
        Appellation_entry.place(x=110, y=60, width=120, height=30)
        Number_entry.place(x=110, y=100, width=120, height=30)
        View_code_entry.place(x=110, y=140, width=120, height=30)
        #Documentcodes_entry.place(x=100, y=180, width=120, height=30)
        #Documentcoder_entry.place(x=100, y=220, width=120, height=30)
        #Reg_date_entry.place(x=100, y=260, width=120, height=30)


        # Создаем кнопку "Редактировать"
        edit_button = Button(z, text='Редактировать', command=lambda:
                             (self.db.updateRecord3(Document_code_1.get(), Appellation_2.get(), Number_3.get(), View_code_4.get(), Documentcodes_5.get(), Documentcoder_6.get(), Reg_date_7.get(), id), self.viewRecords(), self.tableDocuments()))
        edit_button.place(x=10, y=300, width=100, height=30)

        # Создаем кнопку "Закрыть"
        close_button = Button(z, text='Закрыть', command=closeFunc)
        close_button.place(x=115, y=300, width=100, height=30)
        
    def idDelete(self):
        ''' Удаление строки по id из БД '''
        self.selected_item = self.table.selection()[0]  # получаем строку
        values = self.table.item(self.selected_item, option='values')   # получаем значения строки
        delete_id = values[0]   # получаем id строки
        self.db.deleteRecords3(delete_id)   # удаляем строку по полученному id
        
    def lineDelete(self):
        ''' Удаление выбранной строки из таблицы tkinter '''
        self.table.delete(self.selected_item)   # удаляем полученную строку




# ------------------------------------- << TKINTER >> --------------------------------------- #



# ----------------------------- Document_types.tk ---------------------------- #
# ------------------------------------------------------------------------- #

class tkDocument_types():

    def __init__(self):
        self.sale = sale   # экземпляр класса Document_types()
        self.db = db
    def Document_typesButton(self):
        ''' Кнопка для открытия таблицы и её функций '''
        def unionFunc():
            ''' Компонует все кнопки функции выше '''
            def addWindow():
                ''' Создание нового окна для кнопки <Добавить> '''
                def closeFunc():
                    s.destroy() # закрываем окно

                # Создаем новое окно
                s = Toplevel()
                s.geometry('250x200')
                s.title('Add')
                s.resizable(False, False)

                view_code_label = Label(s, text='Код вида').place(x=10, y=60, width=70, height=30)
                name_label = Label(s, text='Нaзвание').place(x=10, y=10, width=70, height=30)
                
                name_1 = StringVar()
                name_2 = StringVar()

                view_code_entry = Entry(s, width=50, textvariable=name_1).place(x=100, y=60, width=100, height=30)
                name_entry = Entry(s, width=50, textvariable=name_2).place(x=100, y=10, width=100, height=30)

                
                add_button = Button(s, text='Добавить', command=lambda:
                                    (self.db.records1(name_1.get(), name_2.get()), self.sale.viewRecords(), self.sale.tableDocument_types()))
                add_button.place(x=10, y=160, width=100, height=30)

                close_button = Button(s, text='Закрыть', command=closeFunc)
                close_button.place(x=115, y=160, width=100, height=30)

            self.add_image = tk.PhotoImage(file='add.png')
            Document_types_add_button = Button(root, text='Добавить', image=self.add_image, compound='top', command=addWindow)
            Document_types_add_button.place(x=10, y=50, width=100, height=80)

            self.edit_image = tk.PhotoImage(file='edit.png')
            Document_types_edit_button = Button(root, text='Редактировать', image=self.edit_image, compound='top', command=lambda:
                                             self.sale.editDocument_types())
            Document_types_edit_button.place(x=120, y=50, width=100, height=80)
            
            self.delete_image = tk.PhotoImage(file='delete.png')    
            Document_types_edit_button = Button(root, text='Удалить', image=self.delete_image, compound='top', command=lambda:
                                             (self.sale.idDelete(), self.sale.lineDelete()))
            Document_types_edit_button.place(x=230, y=50, width=100, height=80)

            def ChoosingTheRightOption():
                if column_menu.get() == 'Нaзвание':
                    s = 'Нaзвание'
                    return s
                      
            column_menu = ttk.Combobox(root,values=['Нaзвание'])
            column_menu.place(x=395, y=75, width=110, height=30)
            column_menu.current(0)

            mb = Menubutton(root, text='Сортировка', relief=RAISED)
            mb.place(x=537, y=75, width=100, height=30)
            
            mb.menu = Menu(mb, tearoff=0)
            mb['menu'] = mb.menu
            
            mb.menu.add_command(label='ВЫВОД В ЭКСЕЛЬ СЛУЖЕБОЙ ЗАПИСКИ ПЛАНОВОГО ОТДЕЛА', command=lambda:
                                (self.sale.generalIncreaseSort(ChoosingTheRightOption()), self.sale.tableDocument_types()))
            mb.menu.add_command(label='ВЫВОД ТАБЛИЦЫ', command=lambda:
                                (self.sale.generalIncrease(ChoosingTheRightOption()), self.sale.tableDocument_types()))
            
                
        Document_types_button = Button(root, text='Document_types', command=lambda:
                                    (unionFunc(), self.sale.viewRecords(), self.sale.tableDocument_types()))
        Document_types_button.place(x=10, y=10, width=100, height=30)

# ------------------------------ Departments.tk ----------------------------- #
# ------------------------------------------------------------------------- #

class tkDepartments():

    def __init__(self):
        self.cust = cust   # экземпляр класса Departments()
        self.db = db
    def DepartmentsButton(self):
        ''' Кнопка для открытия таблицы и её функций '''
        def unionFunc():
            ''' Компонует все кнопки функции выше '''
            def addWindow():
                ''' Создание нового окна для кнопки <Добавить> '''
                def closeFunc():
                    s.destroy() # закрываем окно

                # Создаем новое окно
                s = Toplevel()
                s.geometry('250x200')
                s.title('Add')
                s.resizable(False, False)

                department_code_label = Label(s, text='Код отдела').place(x=10, y=10, width=80, height=30)
                title_label = Label(s, text='Название').place(x=10, y=60, width=80, height=30)
                
                name_1 = StringVar()
                name_3 = StringVar()


                department_code_entry = Entry(s, width=50, textvariable=name_1).place(x=130, y=10, width=100, height=30)
                title_entry = Entry(s, width=50, textvariable=name_3).place(x=130, y=60, width=100, height=30)


                add_button = Button(s, text='Добавить', command=lambda:
                                    (self.db.records2(name_1.get(), name_3.get()), self.cust.viewRecords(), self.cust.tableDepartments()))
                add_button.place(x=10, y=150, width=100, height=30)

                close_button = Button(s, text='Закрыть', command=closeFunc)
                close_button.place(x=115, y=150, width=100, height=30)

            self.add_image = tk.PhotoImage(file='add.png')
            Document_types_add_button = Button(root, text='Добавить', image=self.add_image, compound='top', command=addWindow)
            Document_types_add_button.place(x=10, y=50, width=100, height=80)

            self.edit_image = tk.PhotoImage(file='edit.png')
            Document_types_edit_button = Button(root, text='Редактировать', image=self.edit_image, compound='top', command=lambda:
                                             self.cust.editDepartments())
            Document_types_edit_button.place(x=120, y=50, width=100, height=80)
            
            self.delete_image = tk.PhotoImage(file='delete.png')    
            Document_types_edit_button = Button(root, text='Удалить', image=self.delete_image, compound='top', command=lambda:
                                             (self.cust.idDelete(), self.cust.lineDelete()))
            Document_types_edit_button.place(x=230, y=50, width=100, height=80)
            

        Departments_button = Button(root, text='Departments', command=lambda:
                                  (unionFunc(), self.cust.viewRecords(), self.cust.tableDepartments()))
        Departments_button.place(x=120, y=10, width=100, height=30)



# ------------------------------- Documents.tk ------------------------------- #
# ------------------------------------------------------------------------- #

class tkDocuments():

    def __init__(self):
        self.orde = orde   # экземпляр класса Documents()
        self.db = db
    def DocumentsButton(self):
        ''' Кнопка для открытия таблицы и её функций '''
        def unionFunc():
            ''' Компонует все кнопки функции выше '''
            def addWindow():
                ''' Создание нового окна для кнопки <Добавить> '''
                def closeFunc():
                    s.destroy() # закрываем окно



                # Создаем новое окно
                s = Toplevel()
                s.geometry('280x350')
                s.title('Add')
                s.resizable(False, False)


                Document_code_label = Label(s, text='Код документа').place(x=20, y=10, width=100, height=30)
                Appellation_label = Label(s, text='Название').place(x=20, y=60, width=100, height=30)
                Number_label = Label(s, text='Номер').place(x=20, y=100, width=100, height=30)
                View_code_label = Label(s, text='Код_вида').place(x=20, y=140, width=100, height=30)
                Documentcodes_label = Label(s, text='Код_отдела-отправителя').place(x=20, y=180, width=135, height=30)
                Documentcoder_label = Label(s, text='Код_отдела-получателя').place(x=20, y=220, width=135, height=30)
                Reg_date_label = Label(s, text='Дата регистрации').place(x=20, y=260, width=120, height=30)
                
                
                
                
                name_1 = StringVar()
                name_2 = StringVar()
                name_3 = StringVar()
                name_4 = StringVar()
                name_5 = StringVar()
                name_6 = StringVar()
                name_7 = StringVar()


                Document_code_entry = Entry(s, width=50, textvariable=name_1).place(x=155, y=10, width=120, height=30)
                Appellation_entry = Entry(s, width=50, textvariable=name_2).place(x=155, y=60, width=120, height=30)
                Number_entry = Entry(s, width=50, textvariable=name_3).place(x=155, y=100, width=120, height=30)
                View_code_entry = Entry(s, width=50, textvariable=name_4).place(x=155, y=140, width=120, height=30)
                Documentcodes_entry = Entry(s, width=50, textvariable=name_5).place(x=155, y=180, width=120, height=30)
                Documentcoder_entry = Entry(s, width=50, textvariable=name_6).place(x=155, y=220, width=120, height=30)
                Reg_date_entry = Entry(s, width=50, textvariable=name_7).place(x=155, y=260, width=120, height=30)

                
                
                add_button = Button(s, text='Добавить', command=lambda:
                                    (self.db.records3(name_1.get(), name_2.get(), name_3.get(),  name_4.get(),  name_5.get(),  name_6.get(),  name_7.get()), self.orde.viewRecords(), self.orde.tableDocuments()))
                add_button.place(x=10, y=300, width=100, height=30)

                close_button = Button(s, text='Закрыть', command=closeFunc)
                close_button.place(x=115, y=300, width=100, height=30)

            self.add_image = tk.PhotoImage(file='add.png')
            Document_types_add_button = Button(root, text='Добавить', image=self.add_image, compound='top', command=addWindow)
            Document_types_add_button.place(x=10, y=50, width=100, height=80)

            self.edit_image = tk.PhotoImage(file='edit.png')
            Document_types_edit_button = Button(root, text='Редактировать', image=self.edit_image, compound='top', command=lambda:
                                             self.orde.editDocuments())
            Document_types_edit_button.place(x=120, y=50, width=100, height=80)
            
            self.delete_image = tk.PhotoImage(file='delete.png')    
            Document_types_edit_button = Button(root, text='Удалить', image=self.delete_image, compound='top', command=lambda:
                                             (self.orde.idDelete(), self.orde.lineDelete()))
            Document_types_edit_button.place(x=230, y=50, width=100, height=80)

            def ChoosingTheRightOption():
                if column_menu.get() == 'Код документа':
                    s = 'Код документа'
                    return s
                if column_menu.get() == 'Название':
                    s = 'Название'
                    return s
                if column_menu.get() == 'Номер':
                    s = 'Номер'
                    return s
                if column_menu.get() == 'Код_вида':
                    s = 'Код_вида'
                    return s
                if column_menu.get() == 'Код_отдела-отправителя':
                    s = 'Код_отдела-отправителя'
                    return s
                if column_menu.get() == 'Код_отдела-получателя':
                    s = 'Код_отдела-получателя'
                    return s
                if column_menu.get() == 'Дата регистрации':
                    s = 'Дата регистрации'
                    return s


            
            column_menu = ttk.Combobox(root, values=['Код документа','Название', 'Номер', 'Код_вида', 'Код_отдела-отправителя', 'Код_отдела-получателя', 'Дата регистрации'])
            column_menu.place(x=395, y=75, width=110, height=30)
            column_menu.current(0)
                      
            mb = Menubutton (root, text='Сортировка', relief=RAISED)
            mb.place(x=537, y=75, width=100, height=30)
            
            mb.menu =  Menu( mb,tearoff =0 )
            mb['menu'] =  mb.menu
            
            mb.menu.add_command(label='Сортировать по возрастанию', command=lambda:
                                (self.orde.generalIncreaseSort(ChoosingTheRightOption()), self.orde.tableDocuments()))
            
            mb.menu.add_command(label='Сортировать по убыванию', command=lambda:
                                (self.orde.generalDescendingSort(ChoosingTheRightOption()), self.orde.tableDocuments()))

            
            
        Documents_button = Button(root, text='Documents', command=lambda:
                               (unionFunc(), self.orde.viewRecords(), self.orde.tableDocuments()))
        Documents_button.place(x=230, y=10, width=100, height=30)

        
# --------------------------------------- << БД >> ------------------------------------------ #
#ОТДЕЛЬНЫЙ ФАЙЛ "db"
# ------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    
    db = DB1()

    root = tk.Tk()
    root.geometry('830x485')
    root.title('Канцелярия')
    root.resizable(False, False)

    sale = Document_types()
    cust = Departments()
    orde = Documents()

    s = tkDocument_types()
    c = tkDepartments()
    o = tkDocuments()

    s.Document_typesButton()
    c.DepartmentsButton()
    o.DocumentsButton()


    root.mainloop()

# ------------------------------------------------------------------------------------------- #
