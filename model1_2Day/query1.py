import MySQLdb
from db1 import *
import pandas as pd

def data1(LB):
    hostname = 'YOUR_DB_HOST'
    username = 'YOUR_DB_USER'
    password = 'YOUR_DB_PASSWORD'
    database = 'predictive'

    myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)

    a = backlast()
    df = pd.read_sql(a, myConnection, params=[LB])

    myConnection.close()
    return df

