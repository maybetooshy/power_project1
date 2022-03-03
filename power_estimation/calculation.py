
import sqlite3

def calculation_test():
    conn = sqlite3.connect('C:/Users/admin/workspace2/power_project1/db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM power_estimation_parameter")
    
    c.execute("UPDATE power_estimation_parameter SET icc2 = ? WHERE name = ?", ('5312', 'nvpp'))
    conn.commit()    
    print(c.fetchall())

