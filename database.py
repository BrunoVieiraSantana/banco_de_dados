import psycopg2


conn = psycopg2.connect(dbname = "Multas" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )
cursor = conn.cursor()

def criartabelaMotorista():
    sql = ('''
    create table "Motoristas"(
    "id_motorista" int GENERATED ALWAYS AS IDENTITY,
    "nome" varchar(255) not null,
    "cpf" char(11) not null,
    "cnh" char(11) not null,
    primary key ("id_motorista")
    )
    ''')
    return sql

def criartabelaAutomovel():
    sql = ('''
    create table "Automoveis"(
    "id_automovel" int GENERATED ALWAYS AS IDENTITY,
    "placa" char(7) not null,
    "chassi" char(17) not null,
    "tipo" varchar(255) not null,
    "id_motorista" int,
    primary key ("id_automovel"),

    CONSTRAINT fk_motorista
      FOREIGN KEY ("id_motorista")
      REFERENCES "Motoristas"("id_motorista")
    )
    ''')
    return sql


def criartabelaMulta():
    sql = (''' 
    create table "Multas"(
    "id_multa" int GENERATED ALWAYS AS IDENTITY,
    "valor" float(2) not null,
    "data" char(8) not null,
    "id_motorista" int,
    "id_automovel" int,
    primary key("id_multa"),

    CONSTRAINT fk_motorista
      FOREIGN KEY ("id_motorista")
      REFERENCES "Motoristas"("id_motorista"),

    CONSTRAINT fk_automovel
      FOREIGN KEY ("id_automovel")
      REFERENCES "Automoveis"("id_automovel")
    )
    ''')
    return sql

# ---------------------------------------------------------------------------------------------------------------------------------------------------

def verMotorista():
    cursor.execute('''
    select * from "Motoristas"
    order by "id_motorista" ASC
''')
    a = cursor.fetchall()
    
    return a

def verAutomoveis():
    cursor.execute('''
    select * from "Automoveis"
    order by "id_automovel" ASC
''')
    a = cursor.fetchall()
    
    return a

def verMultas():
    cursor.execute('''
    select * from "Multas"
    order by "id_multa" ASC
''')
    a = cursor.fetchall()
    
    return a

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def buscarMotorista(variavel):
    cursor.execute(f'''
    select * from "Motoristas"
    where "nome" = '{variavel}' or "cpf" = '{variavel}'
    ''')

    a = cursor.fetchall()
    return a

def buscarAutomovel(variavel):
    cursor.execute(f'''
    select * from "Automoveis"
    where "placa" = '{variavel}' or "id_automovel" = '{variavel}'
    ''')

    a = cursor.fetchall()
    return a

def buscarMulta(variavel):
    cursor.execute(f'''
    select * from "Multas"
    where "id_multa" = '{variavel}' or "data" = '{variavel}'
    ''')

    a = cursor.fetchall()
    return a

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def inserirMotorista(nome,cpf,cnh):
    cursor.execute(f'''
    insert into "Motoristas"
    values (default,'{nome}', '{cpf}', '{cnh}')
    ''')
    conn.commit()


def inserirAutomovel(placa,chassi,tipo):
    cursor.execute(f'''
    insert into "Automoveis"
    values (default,'{placa}', '{chassi}', '{tipo}')
    ''')
    conn.commit()

    
def inserirMulta(valor,data,motorista, automovel):
    cursor.execute(f'''
    insert into "Multas"
    values (default,'{valor}', '{data}', '{motorista}', '{automovel}')
    ''')
    conn.commit()

def atualizarMotorista(id,nome,cpf,cnh):
    cursor.execute(f'''
    UPDATE "Motoristas"
    SET nome = '{nome}', cpf= '{cpf}', cnh= '{cnh}'
    WHERE id_motorista = '{id}';
    ''')
    conn.commit()
    



# cursor.execute(criartabelaMotorista())
# conn.commit()
# cursor.execute(criartabelaAutomovel())
# conn.commit()
# cursor.execute(criartabelaMulta())
# conn.commit()



# alunos = verMotorista()
# for aluno in alunos:
#     print(aluno)