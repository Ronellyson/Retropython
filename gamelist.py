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

def countItems():
      return crudService.countItems(cur,'Games')
   # cur.execute("CREATE TABLE Games(Id INT, nome TEXT,categoria Text, imagem str)")
   # cur.execute("INSERT INTO Games VALUES(1,'Junk Jungle' , 'Jogo de exploração de masmorra' ,'img/Junk Jungle.png')")
   # cur.execute("INSERT INTO Games VALUES(2,'Alien_Conquer' , 'Shoot ´em Up' ,'img/Alien_Conquer.png')")
   # cur.execute("INSERT INTO Games VALUES(3,'Mystic Mine','Puzze','img/Mystic Mine.png')")
   # cur.execute("INSERT INTO Games VALUES(4,'Pixelman 3','Plataforma','img/Pixelman 3.png')") 

