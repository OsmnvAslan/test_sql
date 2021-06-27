import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

#  Create table
sql__inti_file = open("init.sql")
sql__init_as_string = sql__inti_file.read()
cur.executescript(sql__init_as_string)

# Execute queries
sql__query_file = open("query.sql")
sql__queries = sql__query_file.read()
sql_commands = sql__queries.split(';')

# Check queries
i: int = 0
for command in sql_commands:
    cur.execute(command)
    rows = cur.fetchall()
    if i == 0:
        try:
            if rows[0][0] == 'Mark' and rows[1][0] == 'David' and rows[2][0] == 'Kim':
                print('Первое заданиче выполнено успешно')
            else:
                print('Первое заданиче не выполнено ')
        except:
            print('Выборка не соответствует условию')
    elif i == 1:
        try:
            if rows[0][0] == 2:
                print('Второе заданиче выполнено успешно')
            else:
                print('Второе заданиче не выполнено ')
        except:
            print('Выборка не соответствует условию')
    elif i == 2:
        try:
            if rows[0][0] == 105000:
                print('Третье заданиче выполнено успешно')
            else:
                print('Третье заданиче не выполнено ')
        except:
            print('Выборка не соответствует условию')
    i += 1

con.close()
