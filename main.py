import random
import mysql.connector
import datetime 

big_dataDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

alturas = [random.uniform(1.30, 2.15) for _ in range(1000)]

estados = [
    "Acre",
    "Alagoas",
    "Amapá",
    "Amazonas",
    "Bahia",
    "Ceará",
    "Distrito Federal",
    "Espírito Santo",
    "Goiás",
    "Maranhão",
    "Mato Grosso",
    "Mato Grosso do Sul",
    "Minas Gerais",
    "Pará",
    "Paraíba",
    "Paraná",
    "Pernambuco",
    "Piauí",
    "Rio de Janeiro",
    "Rio Grande do Norte",
    "Rio Grande do Sul",
    "Rondônia",
    "Roraima",
    "Santa Catarina",
    "São Paulo",
    "Sergipe",
    "Tocantins"
]
sexo = ['F', 'M']
altura_minima = min(alturas)
altura_maxima = max(alturas)

media = sum(alturas) / len(alturas)
abaixo_media = 0

# Este código passa por todos os valores do
# array alturas[1000] e os retorna através do 
# "x" em: 
#    print('{:.2f}'.format(x))
for x in alturas:
    if x < media:
        abaixo_media += 1

    print('{:.2f}'.format(x))

print(f'Altura mínima: {altura_minima:.2f}\nAltura máxima: {altura_maxima:.2f}\nMédia: {media:.2f}')
print(f'{abaixo_media} pessoas estão abaixo da média.')

if input("================\nDeseja continuar? S/N\nR: ").upper() == "S":
    cursor = big_dataDB.cursor()
    
    # Redefinindo a estrutura do Banco de Dados
    cursor.execute("create database if not exists big_data")
    cursor.execute("use big_data")
    cursor.execute("drop table if exists pessoas")
    cursor.execute("""create table pessoas(
	                    codigo int primary key auto_increment,
                        altura float not null,
                        sexo enum('F', 'M') not null,
                        data_nascimento date not null,
                        estado varchar(400) not null
)                  """)
    # Inserção dos dados gerados
    for valA in range(0, 1000):
        valS = random.randint(0, 1)
        valU = random.randint(0, 26)
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)
        getAno = datetime.date.today() 
        # Máx: Ano atual - 10; Min: Ano atual - 100
        # Optei pelo máximo ser este para que as pessoas geradas tenham no mínimo 10 anos de idade
        ano = random.randint(getAno.year - 100, getAno.year - 10)
        
        cursor.execute(f"insert into pessoas(altura, sexo, estado, data_nascimento) values ({alturas[valA]:.2f}, '{sexo[valS]}', '{estados[valU]}', '{ano}-{mes}-{dia}')")
        big_dataDB.commit()
        print(f"ID: {cursor.lastrowid} inserted.")

    if input("================\nDeseja ver os valores inseridos? S/N\nR: ").upper() == "S":
        # Exibir os dados da tabela
        cursor.execute("select * from pessoas")
        resultado = cursor.fetchall()

        for x in resultado:
            print(x)
        
        cursor.close()
        big_dataDB.close()
else:
    exit