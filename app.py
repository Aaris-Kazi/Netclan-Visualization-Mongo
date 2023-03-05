from flask import Flask, redirect, render_template, url_for, request
from flask_restful import Resource, Api
from flask_cors import CORS
from mongo import  sumofAll, sumofFilter

app = Flask(__name__)
CORS(app)


@app.route('/')
def graph():
    return render_template('index.html')


@app.route('/search', methods = ["GET","POST"])
def search():
    if request.method == "GET":
        search = request.args.get('search')
        x, y = sumofAll(str(search).lower())
        return render_template('index.html', topic = search, x = x, y = y, x_label = search, y_label = 'sum')
    else:
        return redirect("/")
    

@app.route('/filter', methods = ["GET","POST"])
def filter():
    if request.method == "GET":
        search = request.args.get('search')
        filter = request.args.get('filter')
        print(search, filter)
        filter = str(filter)
        filter = filter.replace(" ", "_")
        x,y = sumofFilter(str(search).lower(), filter.lower())
        return render_template('index.html', topic = search, x = x, y = y, x_label = search, y_label = filter)
    
    

if __name__ == '__main__':
    app.run(debug=True)
    