import pandas as pd
import sqlite3

def calculation_test():
    conn = sqlite3.connect('C:/Users/admin/workspace2/power_project1/db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM power_estimation_parameter")
    
    c.execute("UPDATE power_estimation_parameter SET icc2 = ? WHERE name = ?", ('5312', 'nvpp'))
    conn.commit()    
    print(c.fetchall())

def update_ctrl(name):
    ctrl = pd.read_csv('C:/Users/admin/workspace2/power_project1/database/ctrl/'+name+'.txt')

    conn = sqlite3.connect('C:/Users/admin/workspace2/power_project1/db.sqlite3')
    c = conn.cursor()

    ### 이미 잇는거면 패스하도록? name이 필요하겠네 ! db 다시만들기 ㄱㄱ (done)
    ### sqlite3 다루는건 html 만들고 해보기!
    data_exist = c.execute("SELECT name from power_estimation_ctrl").fetchall()

    for n in data_exist: ### if_exists 써도 됨
        if n == name:
            return 
################################

    cmd = "INSERT INTO "+"power_estimation_ctrl"+" VALUES (?,?,?,?,?,?)"

    c.execute(cmd, [i for i in list(ctrl.loc[0][0].split(' '))])
    conn.commit()