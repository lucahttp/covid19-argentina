from flask import Flask, render_template, request

app = Flask(__name__)

def sumar(nana,nanana):
    return nana +" - "+ nanana

@app.route('/', methods=['GET', 'POST'])
def root():
	return "intenta usando postman"



@app.route('/query', methods=['GET', 'POST'])
def getdetails():
    global name
    if request.method == 'POST':
        query = request.form['query']
        name = request.form['name']
        #return render_template('new.html', q=query, s=sems)
    return sumar(query,name)


if __name__ == '__main__':
    app.run(debug=True)

