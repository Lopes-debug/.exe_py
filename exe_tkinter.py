from selenium import webdriver
import pandas as pd
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

#Lib para usuário selecionar arquivo desejado
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox

driver = webdriver.Chrome()

janela_web = Tk()  #code padrão
web = tkinter.filedialog.askopenfilename(title= 'Selecione o arquivo web')  #abrir janela interativa para definir arquivo
janela_web.destroy()  #code padrão

# carregar planilha
janela = Tk()  #code padrão
arquivo = tkinter.filedialog.askopenfilename(title= 'Selecione o arquivo excel')  #janela interativa para definir arquivo
janela.destroy()  #code padrão
sheet = pd.read_excel(arquivo)

# preencher formulario com dados da planilha
for index in sheet.index:
    nome = sheet.loc[index, 'Nome']
    advogado = sheet.loc[index, 'Advogado']
    processo = sheet.loc[index, 'Processo']
    cidade = sheet.loc[index, 'Cidade']

    driver.get(web)

    drop_menu = driver.find_element(By.CLASS_NAME, 'dropdown-menu')  #find element in the page
    move = ActionChains(driver).move_to_element(drop_menu).perform()  #move mouse to element
    if cidade == 'Distrito Federal':
        driver.find_element(By.XPATH, '/html/body/div/div/div/a[1]').click()
    elif cidade == ' Rio de Janeiro':
        driver.find_element(By.XPATH, '/html/body/div/div/div/a[2]').click()
    else:
        driver.find_element(By.XPATH, '/html/body/div/div/div/a[3]').click()

    indice = index + 1 
    newaba = driver.window_handles[indice]    
    driver.switch_to.window(newaba)

    driver.find_element(By.ID, 'nome').send_keys(nome)
    driver.find_element(By.ID, 'advogado').send_keys(advogado)
    driver.find_element(By.ID, 'numero').send_keys(processo)
    driver.find_element(By.CLASS_NAME,'registerbtn').click()
    # sleep(1)
    alerta = driver.switch_to.alert
    alerta.accept()
    
    while True:
        try:
            alerta2 = driver.switch_to.alert
            break
        except:
            sleep(1)
        
    if 'Nenhum processo encontrado!' in alerta2.text:
        sheet.loc[index, 'Status'] = 'Encontrado'
    else:
       sheet.loc[index, 'Status'] = 'Não encontrado'
    
    origin = driver.window_handles[0]
    driver.switch_to.window(origin)

print(sheet)
driver.quit()
print('Finish!')
