from flask import Flask, redirect, render_template, url_for, request
from mongo import show_sector, var_graph
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sector_name, sector_size = show_sector()

@app.route('/graph')
def index():
    return render_template('index.html', name = sector_name, size = sector_size)

@app.route('/')
def graph():
    x, y = [],[]
    variables = ['intensity', 'likelihood', 'relevance', 'country', 'topic', 'region', 'city']
    filters = ['end_year', 'topic', 'sector', 'region', 'pestle', 'country', 'city']
    return render_template('index.html', var = variables, filters = filters, name = x, size = y, topic = "")

@app.route('/graph_operation', methods = ["GET","POST"])
def graph_op():
    var = request.form["variables"]
    fil = request.form["filters"]
    x, y = var_graph(var, fil)
    variables = ['intensity', 'likelihood', 'relevance', 'country', 'topic', 'region']
    filters = ['end_year', 'topic', 'sector', 'region', 'pestle', 'country', 'city']
    # print(x,y)
    return render_template('graph.html', var = variables, filters = filters, name = x, size = y, topic=var)

# /search?search=RELEVANCE
@app.route('/search', methods = ["GET","POST"])
def search():
    if request.method == "GET":
        search = request.args.get('search')
        print(search)
        return redirect('/')
    else:
        return redirect("/")
    

if __name__ == '__main__':
    app.run(debug=True)
    