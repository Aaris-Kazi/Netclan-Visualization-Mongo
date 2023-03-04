from flask import Flask, redirect, render_template, url_for, request
from flask_restful import Resource, Api
from flask_cors import CORS
from mongo import show_sector, var_graph, sumofAll, sumofFilter

app = Flask(__name__)
CORS(app)

sector_name, sector_size = show_sector()

@app.route('/graph')
def index():
    return render_template('index.html', name = sector_name, size = sector_size)

@app.route('/')
def graph():
    return render_template('index.html')

@app.route('/graph_operation', methods = ["GET","POST"])
def graph_op():
    var = request.form["variables"]
    fil = request.form["filters"]
    x, y = var_graph(var, fil)
    variables = ['intensity', 'likelihood', 'relevance', 'country', 'topic', 'region']
    filters = ['end_year', 'topic', 'sector', 'region', 'pestle', 'country', 'city']
    # print(x,y)
    return render_template('graph.html', var = variables, filters = filters, name = x, size = y, topic=var)


@app.route('/search', methods = ["GET","POST"])
def search():
    if request.method == "GET":
        search = request.args.get('search')
        x, y = sumofAll(str(search).lower())
        return render_template('index.html', topic = search, x = x, y = y, x_label = search, y_label = 'sum')
    else:
        return redirect("/")

# http://127.0.0.1:5000/filter?search=RELEVANCE&&filter=end_year
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
    # return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)
    