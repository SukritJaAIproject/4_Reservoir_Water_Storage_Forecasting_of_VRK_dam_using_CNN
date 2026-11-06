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
    df = pd.read_sql(a, myConnection)

    myConnection.close()
    return df

