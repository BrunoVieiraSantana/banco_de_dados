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


def criartabelaMotorista(conexao):
    sql = conexao.manipularBanco ('''
    create table "Motoristas"(
    "id_motorista" int GENERATED ALWAYS AS IDENTITY,
    "nome" varchar(255) not null,
    "cpf" char(11) not null unique,
    "cnh" char(11) not null unique,
    primary key ("id_motorista")
    )
    ''')
    return sql

def criartabelaAutomovel(conexao):
    sql = conexao.manipularBanco ('''
    create table "Automoveis"(
    "id_automovel" int GENERATED ALWAYS AS IDENTITY,
    "placa" char(7) not null unique,
    "chassi" char(17) not null unique,
    "tipo" varchar(255) not null,
    "id_motorista" int not null,
    primary key ("id_automovel"),

    CONSTRAINT fk_motorista
      FOREIGN KEY ("id_motorista")
      REFERENCES "Motoristas"("id_motorista")
    )
    ''')
    return sql


def criartabelaMulta(conexao):
    sql = conexao.manipularBanco (''' 
    create table "Multas"(
    "id_multa" int GENERATED ALWAYS AS IDENTITY,
    "valor" float(2) not null,
    "data" timestamp default CURRENT_TIMESTAMP(0),
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

def criartabelaLogin(conexao):
    sql = conexao.manipularBanco ('''
    create table "Login"(
    "id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "login" varchar(255) not null,
    "senha" varchar(255) not null,
    "data_nascimento" char(10),
    "email" varchar(255) 
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
    busca = 0
    buscarAutomovel = conexao.consultarBanco(f'''
    select * from "Automoveis"
    where "placa" = '{variavel}'
    ''')
    busca = buscarAutomovel
    if len(buscarAutomovel) == 0:
        buscarAutomovel2 = conexao.consultarBanco(f'''
        select * from "Automoveis"
        where "id_automovel" = {variavel}
        ''')
        busca = buscarAutomovel2
    return busca

def buscarMulta(conexao,variavel):
    buscarMulta = conexao.consultarBanco(f'''
    select * from "Multas"
    where "id_multa" = {variavel}
    ''')
    return buscarMulta

def buscarCNHMulta(conexao,variavel):
    id_motorista = conexao.consultarBanco(f'''
    select id_motorista from "Motoristas"
    where "cnh" = '{variavel}'
    ''')[0][0]

    buscarMotorista = conexao.consultarBanco(f'''
    select * from "Multas"
    where "id_motorista" = '{id_motorista}'
    ''')
    return buscarMotorista


# Inserir informações nas tabelas --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def inserirMotorista(conexao,nome,cpf,cnh):
    if len(cpf) == 11 and len(cnh) == 11:
        motorista = conexao.manipularBanco(f'''
        insert into "Motoristas"
        values (default,'{nome}', '{cpf}', '{cnh}')
        ''')
    else:
        return False


def inserirAutomovel(conexao,placa,chassi,tipo, id_motorista):
    if len(placa) == 7 and len(chassi) == 17:
        placa2 = placa.upper()
        automovel = conexao.manipularBanco(f'''
        insert into "Automoveis"
        values (default,'{placa2}', '{chassi}', '{tipo}', '{id_motorista}')
        ''')
    else:
        return False

    
def inserirMulta(conexao,valor,data,motorista,automovel):
    busca = 0
    valor2 = valor.replace(',','.')
    if len(data) == 0:
        Multa2 = conexao.manipularBanco(f'''
        insert into "Multas"
        values (default,'{valor2}', default, '{motorista}', '{automovel}')
        ''')
        busca = Multa2
    else:
        Multa = conexao.manipularBanco(f'''
        insert into "Multas"
        values (default,'{valor2}', '{data}', '{motorista}', '{automovel}')
        ''')
        busca = Multa

    return busca

def inserirLogin(conexao,login,senha):
    Login = conexao.manipularBanco(f'''
    insert into "Login"
    values (default,'{login},'{senha}')
    ''')

# Atualizar informações nas tabelas --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def updateMotorista(conexao,id,nome,cpf,cnh):
    if len(cpf) == 11 and len(cnh) == 11:
        updateMotorista = conexao.manipularBanco(f'''
        update "Motoristas"
        set "nome"='{nome}', "cpf"='{cpf}', "cnh"='{cnh}'
        where "id_motorista" = '{id}'
        ''')
    else:
        return False

def updateAutomovel(conexao,id,placa,chassi,tipo, id_motorista):
    if len(placa) == 7 and len(chassi) == 17:
        placa2 = placa.upper()
        updateAutomovel = conexao.manipularBanco(f'''
        update "Automoveis"
        set "placa"='{placa2}', "chassi"='{chassi}', "tipo"='{tipo}', "id_motorista"='{id_motorista}'
        where "id_automovel" = '{id}'
        ''')
    else:
        return False

def updateMulta(conexao,id,valor,data,motorista,automovel):
    valor2 = valor.replace(',','.')
    updateMulta = conexao.manipularBanco(f'''
    update "Multas"
    set "valor"='{valor2}', "data"='{data}', "id_motorista"='{motorista}', "id_automovel" = '{automovel}'
    where "id_multa" = '{id}'
    ''')

def updateLogin(conexao,senhaAntiga,senhaNova):
    verSenhas = conexao.consultarBanco('''
    select "senha" from "Login"
    order by "id" ASC
''')
    controle = False

    for senha in verSenhas:
        if senha[2] == senhaAntiga:
            controle = True
    
    if controle == True:
        updateLogin = conexao.manipularBanco(f'''
        update "Login"
        set "senha" = '{senhaNova}'
        ''')

    if controle == False:
        return "Error!"
    
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

# Ver todas as tabelas ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def vertodasTabelas(conexao):

    multas = conexao.consultarBanco('''
    Select * FROM "Multas"
    ORDER BY "id_multa" ASC
    ''')
    resultado=[]
    for x in multas:
        id = x[0]
        valor = x[1]
        data = x[2]
        nome_motorista = conexao.consultarBanco(f'''
        SELECT "nome" FROM "Motoristas"
        WHERE "id_motorista" = {x[3]}
        ''')[0][0]
        placa = conexao.consultarBanco(f'''
        SELECT "placa" FROM "Automoveis"
        WHERE "id_automovel" = {x[4]}
        ''')[0][0]
        resultado.append((id,valor,data,nome_motorista, placa))
    return resultado

def vertodasTabelasVeiculos(conexao):

    veiculos = conexao.consultarBanco('''
    Select * FROM "Automoveis"
    ORDER BY "id_automovel" ASC
    ''')
    resultado=[]
    for x in veiculos:
        id = x[0]
        placa = x[1]
        chassi = x[2]
        tipo = x[3]
        nome_motorista = conexao.consultarBanco(f'''
        SELECT "nome" FROM "Motoristas"
        WHERE "id_motorista" = {x[4]}
        ''')[0][0]
        resultado.append((id,placa,chassi,tipo,nome_motorista))
    return resultado

# Auto Preencher Multa ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def autoPreencherMulta(conexao):

    multas = conexao.consultarBanco('''
    Select * FROM "Multas"
    ORDER BY "id_multa" ASC
    ''')

    for x in multas:
        
        nome_motorista = conexao.consultarBanco(f'''
        SELECT "nome" FROM "Motoristas"
        WHERE "id_motorista" = {x[3]}
        ''')[0][0]
    

        placa = conexao.consultarBanco(f'''
        SELECT "placa" FROM "Automoveis"
        WHERE "id_automovel" = {x[4]}
        ''')[0][0]
        
    return (nome_motorista, placa)

# Verificar Login -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def verificarLogin(conexao,login,senha):
    verLogin = conexao.consultarBanco('''
    select * from "Login"
    order by "id" ASC
''')

    for x in verLogin:
        if x[1] == login and x[2] == senha:
            return True
        
        else:
            return False

# Funções Auxiliares ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def verNomeMotorista(conexao):
    lista = []
    verMotorista = conexao.consultarBanco('''
    select nome from "Motoristas"
    order by "id_motorista" ASC
''')
    for nome in verMotorista:
        lista.append(nome[0])
    return lista

def buscarNomeMotorista(conexao,variavel):
    id_motorista = conexao.consultarBanco(f'''
    select id_motorista from "Automoveis"
    where "placa" = '{variavel}'
    ''')
    buscarMotorista = conexao.consultarBanco(f'''
    select nome from "Motoristas"
    where "id_motorista" = '{id_motorista[0][0]}'
    ''')
    return buscarMotorista

def buscarIdMotorista(conexao,variavel):
    buscarMotorista = conexao.consultarBanco(f'''
    select id_motorista from "Motoristas"
    where "nome" = '{variavel}'
    ''')
    return buscarMotorista

def buscarPlacaAutomovel(conexao,variavel):
    buscarMotorista = conexao.consultarBanco(f'''
    select id_automovel from "Automoveis"
    where "placa" = '{variavel}'
    ''')
    return buscarMotorista

    

# criartabelaMotorista(con)
# criartabelaAutomovel(con)
# criartabelaMulta(con)
# criartabelaLogin(con)



