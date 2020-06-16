def getItems(cursor, nomeTabela):
   query = 'select * from ' + nomeTabela
   cursor.execute(query);
   currentAll = cursor.fetchall();
   currentAll = list(currentAll) 
   return currentAll;    