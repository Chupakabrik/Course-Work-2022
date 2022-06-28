import sqlite3


class DB1:
    
    def __init__(self):
        # Создаем подключение к БД
        self.conn = sqlite3.connect('Chancellery.db')
        self.cur = self.conn.cursor()
        self.selected_item = 0

        # Создаем таблицу Document_types(Виды документов)
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Document_types (ID_1 integer primary key, 'Код_вида' text, 'Нaзвание' text)''')
        
        # Создаем таблицу Departments(Отделы)
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Departments (ID_2 integer primary key, 'Код_отдела' text, 'Нaзвание' text)''')

        # Создаем таблицу Documents(Документы)
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Documents (ID_3 integer primary key, 'Код документа' text, 'Название' text, 'Номер' text, 'Код_вида' text, 'Код_отдела-отправителя' text, 'Код_отдела-получателя' text, 'Дата регистрации' text)''')
        self.conn.commit()

    def insertDataDocument_types(self, view_code, name):
        ''' Добавление данных для Document_types '''
        self.cur.execute(
            '''INSERT INTO Document_types('Код_вида', 'Нaзвание') VALUES (?, ?)''', (view_code, name))
        self.conn.commit()

    def insertDataDepartments(self, department_code, title):
        ''' Добавление данных для Departments '''
        self.cur.execute(
            '''INSERT INTO Departments('Код_отдела', 'Нaзвание') VALUES (?, ?)''', (department_code, title))
        self.conn.commit()

    def insertDataDocuments(self, Document_code, Appellation, Number, View_code, Documentcodes, Documentcoder, Reg_date):
        ''' Добавление данных для Documents '''
        self.cur.execute(
            '''INSERT INTO Documents('Код документа', 'Название', 'Номер', 'Код_вида', 'Код_отдела-отправителя', 'Код_отдела-получателя', 'Дата регистрации') VALUES (?, ?, ?, ?, ?, ?, ?)''', (Document_code, Appellation, Number, View_code, Documentcodes, Documentcoder, Reg_date))
        self.conn.commit()

    #Методы DB (Виды документов)
    def records1(self, view_code, name):
        ''' Ввод новых данных '''
        self.insertDataDocument_types(view_code, name)

    def updateRecord1(self, view_code, name, ID_1):
        ''' Редактирование данных '''
        self.cur.execute(
            '''UPDATE Document_types SET 'Код_вида'=?, 'Нaзвание'=? WHERE ID_1=?''', (view_code, name, ID_1))
        self.conn.commit()

    def deleteRecords1(self, ID_1):
        ''' Удаление результата '''
        self.cur.execute(
            '''DELETE FROM Document_types WHERE ID_1=?''', (ID_1,))
        self.conn.commit()
    

    #Методы DB (Отделы)
    def records2(self, department_code, title):
        ''' Ввод новых данных '''
        self.insertDataDepartments(department_code, title)

    def updateRecord2(self, department_code, title, ID_2):
        ''' Редактирование данных '''
        self.cur.execute(
            '''UPDATE Departments SET 'Код_отдела'=?, 'Нaзвание'=?  WHERE ID_2=?''', (department_code, title, ID_2))
        self.conn.commit()

    def deleteRecords2(self, ID_2):
        ''' Удаление результата '''
        self.cur.execute(
            '''DELETE FROM Departments WHERE ID_2=?''', (ID_2,))
        self.conn.commit()
        
    #Методы DB (Документы)
    def records3(self, Document_code, Appellation, Number, View_code, Documentcodes, Documentcoder, Reg_date):
        ''' Ввод новых данных '''
        self.insertDataDocuments(Document_code, Appellation, Number, View_code, Documentcodes, Documentcoder, Reg_date)

    def updateRecord3(self, Document_code, Appellation, Number, View_code, Documentcodes, Documentcoder, Reg_date, ID_3):
        ''' Редактирование данных '''
        self.cur.execute(
            '''UPDATE Documents SET 'Код документа'=?, 'Название'=?, 'Номер'=?, 'Код_вида'=?, 'Код_отдела-отправителя'=?, 'Код_отдела-получателя'=?, 'Дата регистрации'=? WHERE ID_3=?''', (Document_code, Appellation, Number, View_code, Documentcodes, Documentcoder, Reg_date, ID_3))
        self.conn.commit()

    def deleteRecords3(self, ID_3):
        ''' Удаление результата '''
        self.cur.execute(
            '''DELETE FROM Documents WHERE ID_3=?''', (ID_3,))
        self.conn.commit()

        
