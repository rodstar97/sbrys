import time
import datetime
import random
import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")#


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry(name = ''):

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = name
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()


def read_from_db(filtername = ''):
    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()
    c.execute("SELECT * FROM stuffToPlot WHERE keyword LIKE 'name%'")#'SELECT * FROM stuffToPlot WHERE value > 2'
    data = c.fetchall()
    #print(data)
    #for row in data:
        #print row[2]
    c.close
    conn.close()
    return data




#create_table()
#data_entry()
def create_database():
    import sqlite3
    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()
    create_table()
    for i in range(100):
        dynamic_data_entry(name = 'name_{0}'.format(i))
        #time.sleep(1)
    c.close
    conn.close()
create_database()
#read_from_db()
c.close
conn.close()