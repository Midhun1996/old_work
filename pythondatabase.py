from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="password",database="classicmodels")

mycur = con.cursor()

# data = [1008,"Johnson",26,"Engineering","Trichy","English"]

# query = f"insert into students values{data[0],data[1],data[2],data[3],data[4],data[5]}"


print(mycur.execute("select * from students"))

# con.commit()



# cols = "id,name,age,education,city,medium".split(",")

# results = mycur.fetchall()

# print(tabulate(results,headers=cols))
