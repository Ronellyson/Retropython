import sqlite3 as lite
import sys
import crudService
import RetroPython
con = lite.connect('./Database/gamelist.db')

with con:
   cur = con.cursor()    
   list=crudService.getItems(cur, 'Games')  

   caminhodaimagem = ''

def getURLDescription(id):
   for descricao in list:
      if(str(descricao[0]) == str(id)):
         return descricao[4]  

def getURLName(id):
   for nome in list:
      if(nome[0]==id):
         return nome[1]

def getURLImage(id):
   for imagem in list:
      if(str(imagem[0]) == str(id)):
         return imagem[3]

def getURLISource(id):
   for source in list:
      if(str(source[0]) == str(id)):
         return source[5]    

def countItems():
      return crudService.countItems(cur,'Games')
  

