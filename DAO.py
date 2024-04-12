import mysql.connector


#print(cnx.is_connected())

cnx = mysql.connector.connect(
        user="root", password="Gatitcha1", host="127.0.0.1", database="db_eventos"
    )
    cursor = cnx.cursor()

def CheckLogin(user, senha):
    query = ('SELECT COUNT(*) FROM tb_usuario WHERE user_email =  %s  AND user_password = %s" 
    )

    cursor.execute(query,[user, senha])

    querySet = cursor.fetchone()

    count = querySet[0]

    if count:
        print(cursor)
    else:
        print("n existe")

    cursor.close()
    cnx.close()

    return count

def CheckCadastro(coluna, atributo):
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
    query = (f"SELECT {campoBuscado} FROM {tabela} WHERE {campoReferencia} = '{valorReferencia}'")

    cursor.execute(query)

    querySet = cursor.fetchone()

    result = querySet[0]

    cursor.close()
    cnx.close()

    return result

def insertCadastro(email, senha, nome1, nome2, cpf):
    query = (
        "INSERT INTO tb_usuario (user_name, user_email, user_password, user_cpf) VALUES ('"
        + nome1 
        + " "
        + nome2 
        + "', '"
        + email
        + "', '"
        + senha
        + "', '"
        + cpf
        + "')"
    )

    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    
