import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              port='3308',
                              database='cadastro')

cursor = cnx.cursor()

query = "SELECT nome, descricao FROM cursos"

cursor.execute(query)

records = cursor.fetchall()

for i in records:
    print(i)

cnx.close()