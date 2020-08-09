from flask import Flask, request, render_template
import pymysql

#db = pymysql.connect("localhost", "username", "password", "database")
db = pymysql.connect("localhost", "root", "", "my")

app = Flask(__name__)
app = Flask(__name__,template_folder='plantillas')
#api = Api(app)
@app.route('/')
def someName():
    cursor = db.cursor()
    sql = "SELECT * FROM myxtable"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)