import sqlite3

cx = sqlite3.connect('banco.db')  # sera criado um arquivo banco.db

cursor = cx.cursor() # cursor
              
              # Criando tabela
                # Aqui criamos os comandos sql    
cursor.execute('''CREATE TABLE cliente
               id INT PRIMARY KEY AUTOINCREMENT NOT NULL,
               nome TEXT NOT NULL,
               idade INT NOT NULL,
               ''')

cursor.execute(''' INSERT INTO banco (id)''')
cx.commit()