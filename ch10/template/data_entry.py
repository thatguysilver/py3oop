# Initializs our sqlite3 database.

import sqlite3

conn = sqlite3.connect('sales.db')

conn.execute('CREATE TABLE Sales (salesperson text, '
            'amt currency, year integer, model text, new boolean)')

conn.execute('INSERT INTO Sales values'
            ' ("Tim", 16000, 2010, "Honda Fit", "true")')

conn.execute('INSERT INTO Sales values'
            ' ("Gayle", 28000, 2009, "Ford Mustang", "true")')

conn.execute("INSERT INTO Sales values"
            " ('Tim', 9000, 2006, 'Ford Focus', 'false')")

conn.execute("INSERT INTO Sales values"
            " ('Gayle', 28000, 2009, 'Ford Mustang', 'true')")
conn.execute("INSERT INTO Sales values"
            " ('Gayle', 50000, 2010, 'Lincoln Navigator', 'true')")
conn.execute("INSERT INTO Sales values"
            " ('Don', 20000, 2008, 'Toyota Prius', 'true')")

conn.commit()
conn.close()

