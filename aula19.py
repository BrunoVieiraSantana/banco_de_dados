import psycopg2
import os

os.system('cls')
con = psycopg2.connect(database="Empresa",user = "postgres",password = "postgres", host="localhost", port="5432")
cursor = con.cursor()

cursor.execute('''
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
AND table_type='BASE TABLE';
''') 
resultado = cursor.fetchall()
controle = False
for nome in resultado:
    if nome[0] == 'Departamento':
        controle = True

if controle == False:
    print('Tabela Departamento foi criada')
    cursor.execute(
"""CREATE TABLE "Departamento"(
"id departamento" int GENERATED ALWAYS AS IDENTITY,
"nome departamento" varchar(255) NOT NULL,
"id gerente" int NOT NULL,
PRIMARY KEY ("id departamento"))"""
)

con.commit()

#----------------------------------------------------------------------
#----------------------------------------------------------------------

cursor.execute('''
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
AND table_type='BASE TABLE';
''') 
resultado = cursor.fetchall()
controle = False
for nome in resultado:
    if nome[0] == 'Funcionario':
        controle = True

if controle == False:
    print('Tabela Funcionario foi criada')
    cursor.execute(
"""CREATE TABLE "Funcionario"(
"id" int GENERATED ALWAYS AS IDENTITY,
"nome" varchar(255) NOT NULL,
"salario" varchar(255) NOT NULL default '0.00',
"cargo" varchar(255) NOT NULL default 'Autônomo',
PRIMARY KEY ("id"))"""
)

con.commit()

while True:
    try:      
        menu_01 = ['1 - Ver Funcionários', '2 - Ver Departamentos', '3 - Inserir Funcionário', '4 - Inserir Departamento', '0 - Sair']
        print(*menu_01, sep='\n')
        escolha_01 = int(input('> '))
        match escolha_01:
            case 1:
                cursor.execute('''SELECT * FROM "Funcionario" ORDER BY "id" ASC''') 
                funcionarios = cursor.fetchall()
                colunas = [coluna[0] for coluna in cursor.description]
                org = '{:<12} '*len(colunas)
                os.system('cls')
                print(org.format(*colunas).title())
                print('-'*57)
                for funcionario in funcionarios:
                    print('{:<12} {:<12} {:<12} {:<12}'.format (*funcionario))
                print('')
            case 2:
                cursor.execute('''SELECT * FROM "Departamento" ORDER BY "id departamento" ASC''') 
                departamentos = cursor.fetchall()
                colunas = [coluna[0] for coluna in cursor.description]
                org = '{:<20} '*len(colunas)
                os.system('cls')
                print(org.format(*colunas).title())
                print('-'*50)
                for departamento in departamentos:
                    print('{:<20} {:<20} {:<20}'.format (*departamento))
                print('')
            case 3:
                os.system('cls')
                print('Digite o nome do novo funcionário')
                nome = input('> ')
                print('Digite o salário do novo funcionário')
                salario = input('> ')
                print('Digite a cargo do novo funcionário')
                cargo = input('> ')

                cursor.execute(f'''INSERT INTO "Funcionario"(nome, salario, cargo) Values('{nome}', '{salario}', '{cargo}')''')
                con.commit()
                os.system('cls')
            case 4:
                os.system('cls')
                print('Digite o nome do novo departamento')
                nome_gerente = input('> ')
                print('Digite o id do gerente deste departamento')
                id_gerente = int(input('> '))

                cursor.execute(f'''INSERT INTO "Departamento"("nome departamento", "id gerente") Values('{nome_gerente}', {id_gerente})''')
                con.commit()
                os.system('cls')
            case 0:
                print('Saindo do programa...')
                break
            case _:
                os.system('cls')
                print('Digite um valor presente no menu')
                print('')
    except:
        os.system('cls')
        print('Valor invalido')
        print('')
