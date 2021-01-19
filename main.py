from flask import Flask, render_template
import pymysql
import os

app = Flask(__name__)


db = pymysql.connect( host=os.environ.get('MYSQL_ADDRESS'), 
                        user="admin", 
                        passwd=os.environ.get('MYSQL_ADMIN_PASSWORD'), 
                        db="free_board", 
                        charset="utf8")

@app.route('/')
def index():
    return render_template('index.html', data_list = data_list)

if __name__ == '__main__':
    sql = 'SELECT * FROM `board`;'
    cur = db.cursor()
    cur.execute(sql)
    data_list = cur.fetchall()

    app.run(host="0.0.0.0", port=5000)
