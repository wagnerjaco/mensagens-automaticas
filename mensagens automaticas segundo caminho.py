from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import pandas as pd

#inporta planilha de contatos 
filepath = 'contacts google.csv'
#trabalha os contatos aplicando a separação de ponto e virgula, coluna name e tira os nomes em branco 
df = pd.read_csv(filepath, sep=',')
contatos_coluna1 = df[["Name"]]
Nomes = contatos_coluna1.dropna()
# abrir navegador em primeiro plano a parte
nave = webdriver.Chrome()
nave.get("https://web.whatsapp.com/")

# tempo para logar no whatsapp
time.sleep(35)
# variavel para conter os nomes  que serão pesquisados
#for nome in Nomes:
for i in range(0, len(Nomes)):
  nome = Nomes.iloc[i]['Name']
 # seleciona o icone contatos 
  time.sleep(2)
  Icone_contatos = nave.find_element( By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[2]/div/span')
  time.sleep(2)
  Icone_contatos.click()
  #selecione e clica na barra de pesquisa de ccontatos 
  search_bar = nave.find_element( By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/div/div[2]/div/div[2]')
  time.sleep(2)
  search_bar.click()
  #envia o nome a ser pesquisado 
  search_bar.send_keys(nome)
  time.sleep(3)
  search_bar.send_keys(Keys.RETURN)
  # espera para encontrar o contato
  time.sleep(5)
  # seleciona a primeira resposta da pesquisa
  #contato = nave.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div')
  #contato.click()
  #seleciona a bara de texto e clica nela 
  contato = nave.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
  time.sleep(2)
  contato.click()
  midia01 = (""" A Chevrolet está lançando novos carros na versão 2023, Por isso estamos com a campanha LIMPA PÁTIO CHEVROLET.                                                       Aqui na Chevrolet é possível !!                                                                                                                R$45.370,02   -   R$645,70(ÚLTIMAS VAGAS)                                                                                                         R$53.619,02   -   R$752,20                                                                                                                                       R$61.868,02   -   R$867,91                                                                                                                                    R$65.992,00   -   R$925,77                                                                                                                                   R$74.241,00   -   R$1.041,49                                                                                                                              R$82.490,00   -   R$1.157,21                                                                                                                              R$85.586,02   -   R$1.200,64                                                                                                                          R$90.090,00   -   R$1.263,83                                                                                                          Foi liberado HOJE, e somente HOJE, Estamos com algumas vagas para um grupo de urgência, acesso à grupos MASTER para qualquer proposta aprovada até 17:00, os grupos da Chevrolet com o maior índice de contemplação do Brasil, sua maior chance de obter um carro novo, SEM ENTRADA e SEM JUROS é HOJE.                                                                                                          ligue agora no 08000311471                                                                                       whatsapp: 011 966336238                                                                                Atalho: wa.me/+5511966336238                                                                                                                                    whatsapp: 011 966336238                                                                                                                                   Atalho: wa.me/+5511966336238 
  """)
  time.sleep(2)
  contato.send_keys(midia01)
  #time.sleep(2)
  #contato = nave.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]')
  #contato.click()
  time.sleep(2)
