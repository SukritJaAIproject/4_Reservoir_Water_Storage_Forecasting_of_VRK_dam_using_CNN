import MySQLdb
from db1 import *
import pandas as pd

def data1(LB):
    hostname = '10.211.1.25'
    username = 'root'
    password = 'opt#565784'
    database = 'predictive'

    myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)

    a = backlast()
    df = pd.read_sql(a, myConnection, params=[LB])

    myConnection.close()
    return df

