import mysql.connector

cnx = mysql.connector.connect(
    user="root", password="05102003M@th", host="127.0.0.1", database="db_eventos"
)
cursor = cnx.cursor()


def CheckLogin(user, senha):
    query = (
        'SELECT COUNT(*) FROM tb_usuario WHERE user_email = "'
        + user
        + '" AND user_password = "'
        + senha
        + '"'
    )

    cursor.execute(query)

    querySet = cursor.fetchone()

    count = querySet[0]

    if count:
        print(cursor)
    else:
        print("n existe")

    cursor.close()
    cnx.close()

    return count


def selectFromWhere(tabela, campoReferencia, valorReferencia, campoBuscado="*"):

    query = (
        "SELECT "
        + campoBuscado
        + "FROM "
        + tabela
        + "WHERE "
        + campoReferencia
        + " = '"
        + valorReferencia
        + "'"
    )

    cursor.execute(query)

    querySet = cursor.fetchone

    result = querySet[0]

    cursor.close()
    cnx.close()

    return result
