import pymysql


def getDBConnection():
    connection = pymysql.connect(
        host="db", user="root", port=3306, password="anybridges04", database="actividad"
    )
    return connection
