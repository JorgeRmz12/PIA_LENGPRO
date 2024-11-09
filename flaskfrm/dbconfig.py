from app import app
import pymysql

def getDBConnection():
    connection = pymysql.connect(
        host='127.0.0.1',         
        user='root',    
        password='anybridges04', 
        database='actividad'  
    )
    return connection