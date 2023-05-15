from faker import Faker
import psycopg2
import random

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


def inserirMotorista(conexao,nome,cpf,cnh):
    motorista = conexao.manipularBanco(f'''
    insert into "Motoristas"
    values (default,'{nome}', '{cpf}', '{cnh}')
    ''')

def inserirAutomovel(conexao,placa,chassi,tipo, id_motorista):
    placa2 = placa.upper()
    automovel = conexao.manipularBanco(f'''
    insert into "Automoveis"
    values (default,'{placa2}', '{chassi}', '{tipo}', '{id_motorista}')
    ''')


def inserirMulta(conexao,valor,data,motorista,automovel):
    Multa = conexao.manipularBanco(f'''
    insert into "Multas"
    values (default,'{valor}', '{data}', '{motorista}', '{automovel}')
    ''')


fake = Faker('pt_BR')
# Motorista
def gerar_motorista():
    for _ in range(50):
        cnh = fake.unique.cpf().replace('.','')
        cnh2 = cnh.replace('-', '')
        cpf = fake.unique.cpf().replace('.','')
        cpf2 = cpf.replace('-', '')
        inserirMotorista(con,fake.name(),cpf2,cnh2)

# Veiculo
def gerar_veiculo():
    Faker.seed(0)
    id_lista = list(range(1, 51))
    for x in range(50):
        placa = fake.bothify(text='???####',letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        chassi = fake.bothify(text='#################')
        lista_tipos = ["Carro", "Moto", "Caminhão", "Ônibus"]
        tipo = random.choice(lista_tipos)
        id_lista = random.sample(range(51), 50)
        inserirAutomovel(con,placa,chassi,tipo, id_lista[x])

def gerar_multa():
    for x in range(50):
        data = fake.date_time_between(start_date='-30y', end_date='now')
        int_num = random.choice(range(10, 2500))
        valor = int_num/10
        motorista = random.sample(range(51), 50)
        veiculo = random.sample(range(21), 20)
        inserirMulta(con,valor,data,motorista[x],veiculo[x])

gerar_multa()
