import csv
import pandas
from datetime import datetime

data = pandas.read_csv("aprendizagem-de-maquina\Aula01\Data_aula01.csv") #Lê arquivos com a biblioteca pandas
coluna = int(input("Qual registro você deseja?"))-1 #Cria um input com o número de registro desejado

data_list = (data["Data_Nascimento"][coluna]).split("-") #recebe o registro referente ao solicitado e o divide em uma lista pelos "-"
data_corrigida = "-".join(data_list) #Junta os elementos da lista em uma str separa por "-"
data_corrigida = datetime.strptime(data_corrigida, "%Y-%m-%d") #Transforma a str em um obj datetime, com padrão americano
data_corrigida = data_corrigida.strftime("%d/%m/%Y") #Transforma a obj datetime em um obj datetime com padrão brasileiro

#O mesmo processo acima se repete abaixo mas com uma data diferente

data_cad_list = (data["Data_Cadastro"][coluna]).split("-")
data_cad_corrigida = "-".join(data_cad_list)
data_cad_corrigida = datetime.strptime(data_cad_corrigida, "%Y-%m-%d")
data_cad_corrigida = data_cad_corrigida.strftime("%d/%m/%Y")

nome = data["Nome"][coluna] 
hora = data["Hora"][coluna]

print(f"Registro {coluna+1} \nNome: {nome}\nData de nascimento: {data_corrigida}\nData de cadastro: {data_cad_corrigida}")