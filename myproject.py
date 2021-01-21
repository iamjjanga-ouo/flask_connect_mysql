from flask import Flask, render_template
import pymysql
import os

application = Flask(__name__)


db = pymysql.connect( host=os.environ.get('MYSQL_ADDRESS'), 
                        user="admin", 
                        passwd=os.environ.get('MYSQL_ADMIN_PASSWORD'), 
                        db="free_board", 
                        charset="utf8")

@application.route('/')
def index():
    sql = 'SELECT * FROM `board`;'
    cur = db.cursor()
    cur.execute(sql)
    data_list = cur.fetchall()

    return render_template('index.html', data_list = data_list)

if __name__ == '__main__':
    application.run(host="127.0.0.1", port=5000)
