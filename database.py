import psycopg2

class Conexao:

    def __init__(self, dbname, host, port, user, password) -> None:
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password
    
    def consultarBanco(self, sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)

        cursor = conn.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado
    
    def manipularBanco(self,sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)
        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()

        cursor.close()

        conn.close()


con = Conexao(dbname = "Multas" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )


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
    "id_motorista" int not null,
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
    "id_motorista" int not null,
    "id_automovel" int not null,
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

# Ver informações contidas nas tabelas ---------------------------------------------------------------------------------------------------------------------------------------------------

def verMotorista(conexao):
    verMotorista = conexao.consultarBanco('''
    select * from "Motoristas"
    order by "id_motorista" ASC
''')
    
    return verMotorista

def verAutomoveis(conexao):
    verAutomovel = conexao.consultarBanco('''
    select * from "Automoveis"
    order by "id_automovel" ASC
''')
  
    return verAutomovel

def verMultas(conexao):
    verMulta = conexao.consultarBanco('''
    select * from "Multas"
    order by "id_multa" ASC
''')
    
    return verMulta

# Buscar informações especificas nas tabelas -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def buscarMotorista(conexao,variavel):
    buscarMotorista = conexao.consultarBanco(f'''
    select * from "Motoristas"
    where "nome" = '{variavel}' or "cpf" = '{variavel}'
    ''')
    return buscarMotorista

def buscarAutomovel(conexao,variavel):
    buscarAutomovel = conexao.consultarBanco(f'''
    select * from "Automoveis"
    where "placa" = '{variavel}' or "id_automovel" = {variavel}
    ''')
    return buscarAutomovel

def buscarMulta(conexao,variavel):
    buscarMulta = conexao.consultarBanco(f'''
    select * from "Multas"
    where "id_multa" = {variavel} or "data" = '{variavel}'
    ''')
    return buscarMulta

# Inserir informações nas tabelas --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def inserirMotorista(conexao,nome,cpf,cnh):
    motorista = conexao.manipularBanco(f'''
    insert into "Motoristas"
    values (default,'{nome}', '{cpf}', '{cnh}')
    ''')


def inserirAutomovel(conexao,placa,chassi,tipo, id_motorista):
    automovel = conexao.manipularBanco(f'''
    insert into "Automoveis"
    values (default,'{placa}', '{chassi}', '{tipo}', '{id_motorista}')
    ''')

    
def inserirMulta(conexao,valor,data,motorista,automovel):
    Multa = conexao.manipularBanco(f'''
    insert into "Multas"
    values (default,'{valor}', '{data}', '{motorista}', '{automovel}')
    ''')

# Atualizar informações nas tabelas --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def updateMotorista(conexao,id,nome,cpf,cnh):
    updateMotorista = conexao.manipularBanco(f'''
    update "Motoristas"
    set "nome"='{nome}', "cpf"='{cpf}', "cnh"='{cnh}'
    where "id_motorista" = '{id}'
    ''')

def updateAutomovel(conexao,id,placa,chassi,tipo, id_motorista):
    updateAutomovel = conexao.manipularBanco(f'''
    update "Automoveis"
    set "placa"='{placa}', "chassi"='{chassi}', "tipo"='{tipo}', "id_motorista"='{id_motorista}'
    where "id_automovel" = '{id}'
    ''')

def updateMulta(conexao,id,valor,data,motorista,automovel):
    updateMulta = conexao.manipularBanco(f'''
    update "Multas"
    set "valor"='{valor}', "data"='{data}', "id_motorista"='{motorista}', "id_automovel" = '{automovel}'
    where "id_multa" = '{id}'
    ''')

# Deletar informações nas tabelas ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def deletarMotorista(conexao,id):
    deletarMotorista = conexao.manipularBanco(f'''
    delete from "Motoristas"
    where "id_motorista" = '{id}'
    ''')

def deletarAutomovel(conexao,id):
    deletarAutomovel = conexao.manipularBanco(f'''
    delete from "Automoveis"
    where "id_automovel" = '{id}'
    ''')

def deletarMulta(conexao,id):
    deletarMulta = conexao.manipularBanco(f'''
    delete from "Multas"
    where "id_multa" = '{id}'
    ''')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# print(verMotorista(con))
# print(buscarMotorista(con, "Sherry Birking"))

# print(buscarAutomovel(con, 1))