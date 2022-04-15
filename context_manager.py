import mysql.connector
from tabulate import tabulate

class Dataop:
    def __init__(self,host,user,password,database,ops="R"):
        print('init method called')
        self.ops = ops
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.con = mysql.connector.connect(host=self.host,
                                           user=self.user,
                                           password=self.password,
                                           database=self.database)
  
          
    def __enter__(self):
        self.cur = self.con.cursor()
        return self.cur

      
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        if self.ops in ["C","U","D"]:
            self.con.commit()



cols = "id,name,age,education,city,medium".split(",")     
 
 
# with Dataop(host="localhost",user="root",password="password",database="classicmodels",ops="U")  as cursor:
#     cursor.execute("update students set city = 'Pudhukottai' where id = '1002'")
    
       
with Dataop(host="localhost",user="root",password="password",database="classicmodels",ops="R")  as cursor:
    cursor.execute("describe students")
    result = cursor.fetchall()


print(tabulate(result,cols))
    
