import MySQLdb
from db1 import *
import pandas as pd

def data1():
    hostname = 'YOUR_DB_HOST'
    username = 'YOUR_DB_USER'
    password = 'YOUR_DB_PASSWORD'
    database = 'predictive'

    myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)

    a = backlimit()
    # a = backlast()
    # df = pd.read_sql(a, myConnection, params=[LB])
    df = pd.read_sql(a, myConnection)

    # def doQuery(conn) :
    #     # a = backlimit()
    #     a = backlast()
    #     df = pd.read_sql(a, conn)
    #     return df

    # df = doQuery(myConnection)

    myConnection.close()
    return df

