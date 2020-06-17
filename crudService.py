def getItems(cursor, nomeTabela):
   query = 'select * from ' + nomeTabela
   cursor.execute(query);
   currentAll = cursor.fetchall();
   currentAll = list(currentAll) 
   return currentAll;    


def countItems(cursor, nomeTabela):
   query = 'select Count() from ' + nomeTabela
   cursor.execute(query);
   cursor_fetch = cursor.fetchone()[0]
   print( cursor_fetch )
   return  cursor_fetch ; 