## Formas de converter código no python em código executável com dois clicks em qualquer computador

## Forma 1 - Código simples sem arquivo externo

##conferir se código funciona corretamente
#abrir prompt de comando e navegar até pasta do arquivo .py (dir, cd, cd ..)
#executar código no prompt e conferir se funciona corretamente (python nomedocodigo)
#pip install pyinstaller
#pyinstaller -w nomedoarquivo.py
#criará pastas "build" e "dist" e esta última irá conter a pasta com o programa executável
#zipar pasta com o programa antes de compartilhá-lo


## Forma 2 - Código complexo com arquivos externos

#importar lib tkinter
# from tkinter import *
# import tkinter.filedialog
# from tkinter import messagebox
# janela_web = Tk()  #code padrão
# web = tkinter.filedialog.askopenfilename(title= 'Selecione o arquivo web')  #abrir janela interativa para definir arquivo
# janela_web.destroy()  #code padrão

#conferir se código funciona corretamente
#abrir prompt de comando e navegar até pasta do arquivo .py (dir, cd, cd ..)
#executar código no prompt e conferir se funciona corretamente (python nomedocodigo)
#pip install auto-py-to-exe
#auto-py-to-exe
#Script Location - selecionar arquivo do código .py
#Onefile - One Directory
#Console Window - Console Based
#Additional Files - Add Files - arquivo externo necessário (chromedriver)
#Advanced - How to generate - debug - imports
#Convert .py to .exe
#criará pasta "output" com pasta do programa exe
#zipar pasta que contém o programa e os demais arquivos antes de compartilhar


#Considerar criar ambiente virtual se caso o programa executável estiver excessivamente pesado
#abrir prompt de comando e navegar até pasta desejada
#python -m venv nomedoambiente   - criar amb virtual 
#nomedoambiente\Scripts\activate   - ativar amb virtual criado
#deactivate   - sair do amb virtual

#consultar docs do venv e da lib virtualenv (mais completo)